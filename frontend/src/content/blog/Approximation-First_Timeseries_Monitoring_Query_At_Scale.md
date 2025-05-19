---
title: "Approximation-First Timeseries Monitoring Query At Scale"
description: "Databases (cs.DB)"
url: "https://arxiv.org/abs/arXiv:2505.10560"
type: "paper"
pubDate: "pendiente"
created_at: "2025-05-18 11:14:27.000919"
log_id: 12
sourcename: arXiv CS
author: pendiente
heroImage: /arxiv.jpg
linkDownload: "pendiente"
---

Abstract:Timeseries monitoring systems such as Prometheus play a crucial role in gaining observability of the underlying system components. These systems collect timeseries metrics from various system components and perform monitoring queries over periodic window-based aggregations (i.e., rule queries). However, despite wide adoption, the operational costs and query latency of rule queries remain high. In this paper, we identify major bottlenecks associated with repeated data scans and query computations concerning window overlaps in rule queries, and present PromSketch, an approximation-first query framework as intermediate caches for monitoring systems. It enables low operational costs and query latency, by combining approximate window-based query frameworks and sketch-based precomputation. PromSketch is implemented as a standalone module that can be integrated into Prometheus and VictoriaMetrics, covering 70% of Prometheus' aggregation over time queries. Our evaluation shows that PromSketch achieves up to a two orders of magnitude reduction in query latency over Prometheus and VictoriaMetrics, while lowering operational dollar costs of query processing by two orders of magnitude compared to Prometheus and by at least 4x compared to VictoriaMetrics with at most 5% average errors across statistics. The source code has been made available at this https URL.
