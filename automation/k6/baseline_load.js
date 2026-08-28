/**
 * Grafana k6 Baseline Load Testing Script
 * Workload: 100 Virtual Users (VUs) continuous execution for 60s
 * Target: Nearby Platform REST API & Static Endpoints
 */

import http from 'k6/http';
import { check, sleep, group } from 'k6';
import { Rate, Trend } from 'k6/metrics';

// Custom Metrics
export const errorRate = new Rate('nearby_error_rate');
export const placeDetailLatency = new Trend('nearby_place_detail_duration');
export const searchLatency = new Trend('nearby_search_duration');

export const options = {
  stages: [
    { duration: '10s', target: 50 },   // Warm up ramp to 50 VUs
    { duration: '40s', target: 100 },  // Sustained steady load at 100 VUs
    { duration: '10s', target: 0 }     // Cool down ramp
  ],
  thresholds: {
    'http_req_duration': ['p(95)<300', 'p(99)<600', 'avg<200'],
    'nearby_error_rate': ['rate<0.02'], // Less than 2% errors allowed
    'http_req_failed': ['rate<0.01']
  }
};

const BASE_URL = __ENV.TARGET_URL || 'http://127.0.0.1:8000';

export default function () {
  group('1. Health & Liveness Probes', function () {
    const resHealth = http.get(`${BASE_URL}/health`);
    check(resHealth, {
      'health status is 200': (r) => r.status === 200,
      'health service is online': (r) => r.json('status') === 'healthy'
    }) || errorRate.add(1);
  });

  group('2. Category Discovery & Spatial Search', function () {
    const resCat = http.get(`${BASE_URL}/api/v1/categories`);
    check(resCat, {
      'categories status is 200': (r) => r.status === 200,
      'categories count > 0': (r) => Array.isArray(r.json()) && r.json().length > 0
    }) || errorRate.add(1);

    const startSearch = Date.now();
    const resSearch = http.get(`${BASE_URL}/api/v1/places?limit=10&page=1`);
    searchLatency.add(Date.now() - startSearch);
    check(resSearch, {
      'places list is 200': (r) => r.status === 200
    }) || errorRate.add(1);
  });

  group('3. Place Detail & Review Fetch', function () {
    const startDetail = Date.now();
    const resDetail = http.get(`${BASE_URL}/api/v1/places/1`);
    placeDetailLatency.add(Date.now() - startDetail);
    check(resDetail, {
      'place detail is 200 or 404': (r) => r.status === 200 || r.status === 404
    }) || errorRate.add(1);
  });

  sleep(Math.random() * 0.5 + 0.2); // Pacing between 200ms and 700ms
}
