---
title: "Struct2D: A Perception-Guided Framework for Spatial Reasoning in Large Multimodal Models"
description: "Computer Vision and Pattern Recognition (cs.CV)"
url: "https://arxiv.org/abs/arXiv:2506.04220"
type: "paper"
pubDate: "[Submitted on 4 Jun 2025]"
created_at: "2025-06-05 21:15:40.028138"
log_id: 51
sourcename: arXiv CS
author: "Authors:Fangrui Zhu, Hanhui Wang, Yiming Xie, Jing Gu, Tianye Ding, Jianwei Yang, Huaizu Jiang"
heroImage: /arxiv.jpg
linkDownload: "https://arxiv.org/pdf/2506.04220"
---

Abstract:Unlocking spatial reasoning in Large Multimodal Models (LMMs) is crucial for enabling intelligent interaction with 3D environments. While prior efforts often rely on explicit 3D inputs or specialized model architectures, we ask: can LMMs reason about 3D space using only structured 2D representations derived from perception? We introduce Struct2D, a perception-guided prompting framework that combines bird's-eye-view (BEV) images with object marks and object-centric metadata, optionally incorporating egocentric keyframes when needed. Using Struct2D, we conduct an in-depth zero-shot analysis of closed-source LMMs (e.g., GPT-o3) and find that they exhibit surprisingly strong spatial reasoning abilities when provided with structured 2D inputs, effectively handling tasks such as relative direction estimation and route planning. Building on these insights, we construct Struct2D-Set, a large-scale instruction tuning dataset with 200K fine-grained QA pairs across eight spatial reasoning categories, generated automatically from 3D indoor scenes. We fine-tune an open-source LMM (Qwen2.5VL) on Struct2D-Set, achieving competitive performance on multiple benchmarks, including 3D question answering, dense captioning, and object grounding. Our approach demonstrates that structured 2D inputs can effectively bridge perception and language reasoning in LMMs-without requiring explicit 3D representations as input. We will release both our code and dataset to support future research.
