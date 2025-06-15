---
title: "RecGPT: A Foundation Model for Sequential Recommendation"
description: "Information Retrieval (cs.IR)"
url: "https://arxiv.org/abs/arXiv:2506.06270"
type: "paper"
pubDate: "[Submitted on 6 Jun 2025]"
created_at: "2025-06-09 16:54:24.822769"
log_id: 57
sourcename: arXiv CS
author: "Authors:Yangqin Jiang, Xubin Ren, Lianghao Xia, Da Luo, Kangyi Lin, Chao Huang"
heroImage: /arxiv.jpg
linkDownload: "https://arxiv.org/pdf/2506.06270"
---

Abstract:This work addresses a fundamental barrier in recommender systems: the inability to generalize across domains without extensive retraining. Traditional ID-based approaches fail entirely in cold-start and cross-domain scenarios where new users or items lack sufficient interaction history. Inspired by foundation models' cross-domain success, we develop a foundation model for sequential recommendation that achieves genuine zero-shot generalization capabilities. Our approach fundamentally departs from existing ID-based methods by deriving item representations exclusively from textual features. This enables immediate embedding of any new item without model retraining. We introduce unified item tokenization with Finite Scalar Quantization that transforms heterogeneous textual descriptions into standardized discrete tokens. This eliminates domain barriers that plague existing systems. Additionally, the framework features hybrid bidirectional-causal attention that captures both intra-item token coherence and inter-item sequential dependencies. An efficient catalog-aware beam search decoder enables real-time token-to-item mapping. Unlike conventional approaches confined to their training domains, RecGPT naturally bridges diverse recommendation contexts through its domain-invariant tokenization mechanism. Comprehensive evaluations across six datasets and industrial scenarios demonstrate consistent performance advantages.
