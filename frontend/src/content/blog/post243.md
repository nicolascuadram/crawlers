---
title: "MiniMax-Remover: Taming Bad Noise Helps Video Object Removal"
description: "Computer Vision and Pattern Recognition (cs.CV)"
url: "https://arxiv.org/abs/arXiv:2505.24873"
type: "paper"
pubDate: "[Submitted on 30 May 2025]"
created_at: "2025-06-02 14:41:35.057864"
log_id: 42
sourcename: arXiv CS
author: "Authors:Bojia Zi, Weixuan Peng, Xianbiao Qi, Jianan Wang, Shihao Zhao, Rong Xiao, Kam-Fai Wong"
heroImage: /arxiv.jpg
linkDownload: "https://arxiv.org/pdf/2505.24873"
---

Abstract:Recent advances in video diffusion models have driven rapid progress in video editing techniques. However, video object removal, a critical subtask of video editing, remains challenging due to issues such as hallucinated objects and visual artifacts. Furthermore, existing methods often rely on computationally expensive sampling procedures and classifier-free guidance (CFG), resulting in slow inference. To address these limitations, we propose MiniMax-Remover, a novel two-stage video object removal approach. Motivated by the observation that text condition is not best suited for this task, we simplify the pretrained video generation model by removing textual input and cross-attention layers, resulting in a more lightweight and efficient model architecture in the first stage. In the second stage, we distilled our remover on successful videos produced by the stage-1 model and curated by human annotators, using a minimax optimization strategy to further improve editing quality and inference speed. Specifically, the inner maximization identifies adversarial input noise ("bad noise") that makes failure removals, while the outer minimization step trains the model to generate high-quality removal results even under such challenging conditions. As a result, our method achieves a state-of-the-art video object removal results with as few as 6 sampling steps and doesn't rely on CFG, significantly improving inference efficiency. Extensive experiments demonstrate the effectiveness and superiority of MiniMax-Remover compared to existing methods. Codes and Videos are available at: this https URL.
