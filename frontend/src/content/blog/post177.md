---
title: "The Climb Carves Wisdom Deeper Than the Summit: On the Noisy Rewards in Learning to Reason"
description: "Computation and Language (cs.CL)"
url: "https://arxiv.org/abs/arXiv:2505.22653"
type: "paper"
pubDate: "[Submitted on 28 May 2025]"
created_at: "2025-05-29 19:32:50.895689"
log_id: 36
sourcename: arXiv CS
author: Authors:Ang Lv, Ruobing Xie, Xingwu Sun, Zhanhui Kang, Rui Yan
heroImage: /arxiv.jpg
linkDownload: "https://arxiv.org/pdf/2505.22653"
---

Abstract:Recent studies on post-training large language models (LLMs) for reasoning through reinforcement learning (RL) typically focus on tasks that can be accurately verified and rewarded, such as solving math problems. In contrast, our research investigates the impact of reward noise, a more practical consideration for real-world scenarios involving the post-training of LLMs using reward models. We found that LLMs demonstrate strong robustness to substantial reward noise. For example, manually flipping 40% of the reward function's outputs in math tasks still allows a Qwen-2.5-7B model to achieve rapid convergence, improving its performance on math tasks from 5% to 72%, compared to the 75% accuracy achieved by a model trained with noiseless rewards. Surprisingly, by only rewarding the appearance of key reasoning phrases (namely reasoning pattern reward, RPR), such as ``first, I need to''-without verifying the correctness of answers, the model achieved peak downstream performance (over 70% accuracy for Qwen-2.5-7B) comparable to models trained with strict correctness verification and accurate rewards. Recognizing the importance of the reasoning process over the final results, we combined RPR with noisy reward models. RPR helped calibrate the noisy reward models, mitigating potential false negatives and enhancing the LLM's performance on open-ended tasks. These findings suggest the importance of improving models' foundational abilities during the pre-training phase while providing insights for advancing post-training techniques. Our code and scripts are available at this https URL.
