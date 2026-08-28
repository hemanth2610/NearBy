/**
 * Grafana k6 Stress & Spike Testing Scripts
 * Simulating 200/500 VU Peak Stress and 10x Sudden Spike Bursts
 */

import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '15s', target: 100 },
    { duration: '30s', target: 200 },
    { duration: '30s', target: 500 }, // Peak Stress 500 VUs
    { duration: '15s', target: 0 }
  ],
  thresholds: {
    'http_req_duration': ['p(95)<450', 'p(99)<800'],
    'http_req_failed': ['rate<0.05']
  }
};

const BASE_URL = __ENV.TARGET_URL || 'http://127.0.0.1:8000';

export default function () {
  const endpoints = [
    '/health',
    '/api/v1/categories',
    '/api/v1/places?limit=20',
    '/api/v1/explore?q=beach',
    '/api/v1/system/info'
  ];
  
  const target = endpoints[Math.floor(Math.random() * endpoints.length)];
  const res = http.get(`${BASE_URL}${target}`);
  
  check(res, {
    'status is valid (2xx/3xx/4xx)': (r) => r.status < 500
  });

  sleep(0.1);
}
