---
title: "Zero-Shot Vision Encoder Grafting via LLM Surrogates"
description: "Computer Vision and Pattern Recognition (cs.CV)"
url: "https://arxiv.org/abs/arXiv:2505.22664"
type: "paper"
pubDate: "[Submitted on 28 May 2025]"
created_at: "2025-05-29 19:32:50.895689"
log_id: 36
sourcename: arXiv CS
author: Authors:Kaiyu Yue, Vasu Singla, Menglin Jia, John Kirchenbauer, Rifaa Qadri, Zikui Cai, Abhinav Bhatele, Furong Huang, Tom Goldstein
heroImage: /arxiv.jpg
linkDownload: "https://arxiv.org/pdf/2505.22664"
---

Abstract:Vision language models (VLMs) typically pair a modestly sized vision encoder with a large language model (LLM), e.g., Llama-70B, making the decoder the primary computational burden during training. To reduce costs, a potential promising strategy is to first train the vision encoder using a small language model before transferring it to the large one. We construct small "surrogate models" that share the same embedding space and representation language as the large target LLM by directly inheriting its shallow layers. Vision encoders trained on the surrogate can then be directly transferred to the larger model, a process we call zero-shot grafting -- when plugged directly into the full-size target LLM, the grafted pair surpasses the encoder-surrogate pair and, on some benchmarks, even performs on par with full decoder training with the target LLM. Furthermore, our surrogate training approach reduces overall VLM training costs by ~45% when using Llama-70B as the decoder.
