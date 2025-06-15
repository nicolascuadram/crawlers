---
title: "InstaInpaint: Instant 3D-Scene Inpainting with Masked Large Reconstruction Model"
description: "Computer Vision and Pattern Recognition (cs.CV)"
url: "https://arxiv.org/abs/arXiv:2506.10980"
type: "paper"
pubDate: "[Submitted on 12 Jun 2025]"
created_at: "2025-06-13 13:31:44.378180"
log_id: 13
sourcename: arXiv CS
author: "Authors:Junqi You, Chieh Hubert Lin, Weijie Lyu, Zhengbo Zhang, Ming-Hsuan Yang"
heroImage: /arxiv.jpg
linkDownload: "https://arxiv.org/pdf/2506.10980"
---

Abstract:Recent advances in 3D scene reconstruction enable real-time viewing in virtual and augmented reality. To support interactive operations for better immersiveness, such as moving or editing objects, 3D scene inpainting methods are proposed to repair or complete the altered geometry. However, current approaches rely on lengthy and computationally intensive optimization, making them impractical for real-time or online applications. We propose InstaInpaint, a reference-based feed-forward framework that produces 3D-scene inpainting from a 2D inpainting proposal within 0.4 seconds. We develop a self-supervised masked-finetuning strategy to enable training of our custom large reconstruction model (LRM) on the large-scale dataset. Through extensive experiments, we analyze and identify several key designs that improve generalization, textural consistency, and geometric correctness. InstaInpaint achieves a 1000x speed-up from prior methods while maintaining a state-of-the-art performance across two standard benchmarks. Moreover, we show that InstaInpaint generalizes well to flexible downstream applications such as object insertion and multi-region inpainting. More video results are available at our project page: this https URL.
