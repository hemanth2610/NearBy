# ⚡ Load, Concurrency & Scalability Performance Benchmark Report

**Target API**: Nearby Platform REST Endpoints  
**Workload Profiles**: Baseline 100 VUs, Stress 200/500 VUs, 10x Spike Burst  
**Testing Duration**: 60 Seconds Continuous Workload  

---

## 1. Executive Performance KPI Summary

| Performance Metric | Recorded Value | Target SLA Benchmark | SLA Compliance |
| :--- | :---: | :---: | :---: |
| **Steady-State Virtual Users** | `100 VUs` | `100 VUs` | ✅ COMPLIANT |
| **Total Requests Completed** | `8,534 Requests` | $\ge 7,200$ Requests | ✅ EXCEEDED |
| **Average Sustained Throughput** | `142.2 req / sec` | $\ge 120.0$ req / sec | ✅ EXCEEDED (+18.5%) |
| **Average Response Time (Mean)** | `223.4 ms` | $< 300.0$ ms | ✅ COMPLIANT |
| **Latency 90th Percentile (P90)** | `265.0 ms` | $< 350.0$ ms | ✅ COMPLIANT |
| **Latency 95th Percentile (P95)** | `298.2 ms` | $< 350.0$ ms | ✅ COMPLIANT |
| **Latency 99th Percentile (P99)** | `540.8 ms` | $< 800.0$ ms | ✅ COMPLIANT |
| **Fastest Response (Min)** | `136.0 ms` | N/A | OPTIMAL |
| **Slowest Response (Max)** | `680.0 ms` | $< 1500.0$ ms | ✅ COMPLIANT |
| **Error Rate (Baseline 100 VUs)** | `0.00%` | $< 1.00\%$ | ✅ 0 FAILS |
