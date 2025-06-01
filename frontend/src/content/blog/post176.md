---
title: "VScan: Rethinking Visual Token Reduction for Efficient Large Vision-Language Models"
description: "Computer Vision and Pattern Recognition (cs.CV)"
url: "https://arxiv.org/abs/arXiv:2505.22654"
type: "paper"
pubDate: "[Submitted on 28 May 2025]"
created_at: "2025-05-29 19:32:50.895689"
log_id: 36
sourcename: arXiv CS
author: Authors:Ce Zhang, Kaixin Ma, Tianqing Fang, Wenhao Yu, Hongming Zhang, Zhisong Zhang, Yaqi Xie, Katia Sycara, Haitao Mi, Dong Yu
heroImage: /arxiv.jpg
linkDownload: "https://arxiv.org/pdf/2505.22654"
---

Abstract:Recent Large Vision-Language Models (LVLMs) have advanced multi-modal understanding by incorporating finer-grained visual perception and encoding. However, such methods incur significant computational costs due to longer visual token sequences, posing challenges for real-time deployment. To mitigate this, prior studies have explored pruning unimportant visual tokens either at the output layer of the visual encoder or at the early layers of the language model. In this work, we revisit these design choices and reassess their effectiveness through comprehensive empirical studies of how visual tokens are processed throughout the visual encoding and language decoding stages. Guided by these insights, we propose VScan, a two-stage visual token reduction framework that addresses token redundancy by: (1) integrating complementary global and local scans with token merging during visual encoding, and (2) introducing pruning at intermediate layers of the language model. Extensive experimental results across four LVLMs validate the effectiveness of VScan in accelerating inference and demonstrate its superior performance over current state-of-the-arts on sixteen benchmarks. Notably, when applied to LLaVA-NeXT-7B, VScan achieves a 2.91$\times$ speedup in prefilling and a 10$\times$ reduction in FLOPs, while retaining 95.4% of the original performance.
