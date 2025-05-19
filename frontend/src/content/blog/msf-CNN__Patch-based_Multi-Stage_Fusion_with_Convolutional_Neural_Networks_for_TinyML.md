---
title: "msf-CNN: Patch-based Multi-Stage Fusion with Convolutional Neural Networks for TinyML"
description: "Machine Learning (cs.LG); Performance (cs.PF)"
url: "https://arxiv.org/abs/arXiv:2505.11483"
type: "paper"
pubDate: "pendiente"
created_at: "2025-05-19 16:02:22.715847"
log_id: 23
sourcename: arXiv CS
author: pendiente
heroImage: /arxiv.jpg
linkDownload: "pendiente"
---

Abstract:AI spans from large language models to tiny models running on microcontrollers (MCUs). Extremely memory-efficient model architectures are decisive to fit within an MCU's tiny memory budget e.g., 128kB of RAM. However, inference latency must remain small to fit real-time constraints. An approach to tackle this is patch-based fusion, which aims to optimize data flows across neural network layers. In this paper, we introduce msf-CNN, a novel technique that efficiently finds optimal fusion settings for convolutional neural networks (CNNs) by walking through the fusion solution space represented as a directed acyclic graph. Compared to previous work on CNN fusion for MCUs, msf-CNN identifies a wider set of solutions. We published an implementation of msf-CNN running on various microcontrollers (ARM Cortex-M, RISC-V, ESP32). We show that msf-CNN can achieve inference using 50% less RAM compared to the prior art (MCUNetV2 and StreamNet). We thus demonstrate how msf-CNN offers additional flexibility for system designers.
