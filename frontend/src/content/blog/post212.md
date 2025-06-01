---
title: "LoRAShop: Training-Free Multi-Concept Image Generation and Editing with Rectified Flow Transformers"
description: "Computer Vision and Pattern Recognition (cs.CV)"
url: "https://arxiv.org/abs/arXiv:2505.23758"
type: "paper"
pubDate: "[Submitted on 29 May 2025]"
created_at: "2025-05-31 09:06:40.094566"
log_id: 39
sourcename: arXiv CS
author: Authors:Yusuf Dalva, Hidir Yesiltepe, Pinar Yanardag
heroImage: /arxiv.jpg
linkDownload: "https://arxiv.org/pdf/2505.23758"
---

Abstract:We introduce LoRAShop, the first framework for multi-concept image editing with LoRA models. LoRAShop builds on a key observation about the feature interaction patterns inside Flux-style diffusion transformers: concept-specific transformer features activate spatially coherent regions early in the denoising process. We harness this observation to derive a disentangled latent mask for each concept in a prior forward pass and blend the corresponding LoRA weights only within regions bounding the concepts to be personalized. The resulting edits seamlessly integrate multiple subjects or styles into the original scene while preserving global context, lighting, and fine details. Our experiments demonstrate that LoRAShop delivers better identity preservation compared to baselines. By eliminating retraining and external constraints, LoRAShop turns personalized diffusion models into a practical `photoshop-with-LoRAs' tool and opens new avenues for compositional visual storytelling and rapid creative iteration.
