---
title: "SiLVR: A Simple Language-based Video Reasoning Framework"
description: "Computer Vision and Pattern Recognition (cs.CV)"
url: "https://arxiv.org/abs/arXiv:2505.24869"
type: "paper"
pubDate: "[Submitted on 30 May 2025]"
created_at: "2025-06-02 14:41:35.057864"
log_id: 42
sourcename: arXiv CS
author: "Authors:Ce Zhang, Yan-Bo Lin, Ziyang Wang, Mohit Bansal, Gedas Bertasius"
heroImage: /arxiv.jpg
linkDownload: "https://arxiv.org/pdf/2505.24869"
---

Abstract:Recent advances in test-time optimization have led to remarkable reasoning capabilities in Large Language Models (LLMs), enabling them to solve highly complex problems in math and coding. However, the reasoning capabilities of multimodal LLMs (MLLMs) still significantly lag, especially for complex video-language tasks. To address this issue, we present SiLVR, a Simple Language-based Video Reasoning framework that decomposes complex video understanding into two stages. In the first stage, SiLVR transforms raw video into language-based representations using multisensory inputs, such as short clip captions and audio/speech subtitles. In the second stage, language descriptions are fed into a powerful reasoning LLM to solve complex video-language understanding tasks. To handle long-context multisensory inputs, we use an adaptive token reduction scheme, which dynamically determines the temporal granularity with which to sample the tokens. Our simple, modular, and training-free video reasoning framework achieves the best-reported results on Video-MME (long), Video-MMMU (comprehension), Video-MMLU, CGBench, and EgoLife. Furthermore, our empirical study focused on video reasoning capabilities shows that, despite not being explicitly trained on video, strong reasoning LLMs can effectively aggregate multisensory input information from video, speech, and audio for complex temporal, causal, long-context, and knowledge acquisition reasoning tasks in video. Code is available at this https URL.
