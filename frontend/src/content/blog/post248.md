---
title: "LayerFlow: A Unified Model for Layer-aware Video Generation"
description: "Computer Vision and Pattern Recognition (cs.CV)"
url: "https://arxiv.org/abs/arXiv:2506.04228"
type: "paper"
pubDate: "[Submitted on 4 Jun 2025]"
created_at: "2025-06-05 21:15:40.028138"
log_id: 51
sourcename: arXiv CS
author: "Authors:Sihui Ji, Hao Luo, Xi Chen, Yuanpeng Tu, Yiyang Wang, Hengshuang Zhao"
heroImage: /arxiv.jpg
linkDownload: "https://arxiv.org/pdf/2506.04228"
---

Abstract:We present LayerFlow, a unified solution for layer-aware video generation. Given per-layer prompts, LayerFlow generates videos for the transparent foreground, clean background, and blended scene. It also supports versatile variants like decomposing a blended video or generating the background for the given foreground and vice versa. Starting from a text-to-video diffusion transformer, we organize the videos for different layers as sub-clips, and leverage layer embeddings to distinguish each clip and the corresponding layer-wise prompts. In this way, we seamlessly support the aforementioned variants in one unified framework. For the lack of high-quality layer-wise training videos, we design a multi-stage training strategy to accommodate static images with high-quality layer annotations. Specifically, we first train the model with low-quality video data. Then, we tune a motion LoRA to make the model compatible with static frames. Afterward, we train the content LoRA on the mixture of image data with high-quality layered images along with copy-pasted video data. During inference, we remove the motion LoRA thus generating smooth videos with desired layers.
