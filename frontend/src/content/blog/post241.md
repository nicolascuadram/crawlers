---
title: "ReasonGen-R1: CoT for Autoregressive Image generation models through SFT and RL"
description: "Computer Vision and Pattern Recognition (cs.CV); Computation and Language (cs.CL)"
url: "https://arxiv.org/abs/arXiv:2505.24875"
type: "paper"
pubDate: "[Submitted on 30 May 2025]"
created_at: "2025-06-02 14:41:35.057864"
log_id: 42
sourcename: arXiv CS
author: "Authors:Yu Zhang, Yunqi Li, Yifan Yang, Rui Wang, Yuqing Yang, Dai Qi, Jianmin Bao, Dongdong Chen, Chong Luo, Lili Qiu"
heroImage: /arxiv.jpg
linkDownload: "https://arxiv.org/pdf/2505.24875"
---

Abstract:Although chain-of-thought reasoning and reinforcement learning (RL) have driven breakthroughs in NLP, their integration into generative vision models remains underexplored. We introduce ReasonGen-R1, a two-stage framework that first imbues an autoregressive image generator with explicit text-based "thinking" skills via supervised fine-tuning on a newly generated reasoning dataset of written rationales, and then refines its outputs using Group Relative Policy Optimization. To enable the model to reason through text before generating images, We automatically generate and release a corpus of model crafted rationales paired with visual prompts, enabling controlled planning of object layouts, styles, and scene compositions. Our GRPO algorithm uses reward signals from a pretrained vision language model to assess overall visual quality, optimizing the policy in each update. Evaluations on GenEval, DPG, and the T2I benchmark demonstrate that ReasonGen-R1 consistently outperforms strong baselines and prior state-of-the-art models. More: this http URL.
