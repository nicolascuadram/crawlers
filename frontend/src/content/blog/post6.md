---
title: "Inference-Time Hyper-Scaling with KV Cache Compression"
description: "Machine Learning (cs.LG); Computation and Language (cs.CL)"
url: "https://arxiv.org/abs/arXiv:2506.05345"
type: "paper"
pubDate: "[Submitted on 5 Jun 2025]"
created_at: "2025-06-07 11:30:03.413421"
log_id: 1
sourcename: arXiv CS
author: "Authors:Adrian Łańcucki, Konrad Staniszewski, Piotr Nawrot, Edoardo M. Ponti"
heroImage: /arxiv.jpg
linkDownload: "https://arxiv.org/pdf/2506.05345"
---

Abstract:Inference-time scaling trades efficiency for increased reasoning accuracy by generating longer or more parallel sequences. However, in Transformer LLMs, generation cost is bottlenecked by the size of the key-value (KV) cache, rather than the number of generated tokens. Hence, we explore inference-time hyper-scaling: by compressing the KV cache, we can generate more tokens within the same compute budget and further improve the accuracy of scaled inference. The success of this approach, however, hinges on the ability of compression methods to preserve accuracy even at high compression ratios. To make hyper-scaling practical, we introduce Dynamic Memory Sparsification (DMS), a novel method for sparsifying KV caches that only requires 1K training steps to achieve 8$\times$ compression, while maintaining better accuracy than training-free sparse attention. Instead of prematurely discarding cached tokens, DMS delays token eviction, implicitly merging representations and preserving critical information. We demonstrate the effectiveness of inference-time hyper-scaling with DMS on multiple families of LLMs, showing that it boosts accuracy for comparable inference runtime and memory load. For instance, we enhance Qwen-R1 32B by an average of 9.1 points on AIME 24, 7.6 on GPQA, and 9.6 on LiveCodeBench across compute budgets.
