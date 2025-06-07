---
title: "ContentV: Efficient Training of Video Generation Models with Limited Compute"
description: "Computer Vision and Pattern Recognition (cs.CV)"
url: "https://arxiv.org/abs/arXiv:2506.05343"
type: "paper"
pubDate: "[Submitted on 5 Jun 2025]"
created_at: "2025-06-07 11:30:03.413421"
log_id: 1
sourcename: arXiv CS
author: "Authors:Wenfeng Lin, Renjie Chen, Boyuan Liu, Shiyue Yan, Ruoyu Feng, Jiangchuan Wei, Yichen Zhang, Yimeng Zhou, Chao Feng, Jiao Ran, Qi Wu, Zuotao Liu, Mingyu Guo"
heroImage: /arxiv.jpg
linkDownload: "https://arxiv.org/pdf/2506.05343"
---

Abstract:Recent advances in video generation demand increasingly efficient training recipes to mitigate escalating computational costs. In this report, we present ContentV, an 8B-parameter text-to-video model that achieves state-of-the-art performance (85.14 on VBench) after training on 256 x 64GB Neural Processing Units (NPUs) for merely four weeks. ContentV generates diverse, high-quality videos across multiple resolutions and durations from text prompts, enabled by three key innovations: (1) A minimalist architecture that maximizes reuse of pre-trained image generation models for video generation; (2) A systematic multi-stage training strategy leveraging flow matching for enhanced efficiency; and (3) A cost-effective reinforcement learning with human feedback framework that improves generation quality without requiring additional human annotations. All the code and models are available at: this https URL.
