---
title: "Efficient Knowledge Editing via Minimal Precomputation"
description: "Computation and Language (cs.CL); Artificial Intelligence (cs.AI)"
url: "https://arxiv.org/abs/arXiv:2506.04226"
type: "paper"
pubDate: "[Submitted on 4 Jun 2025]"
created_at: "2025-06-05 21:15:40.028138"
log_id: 51
sourcename: arXiv CS
author: "Authors:Akshat Gupta, Maochuan Lu, Thomas Hartvigsen, Gopala Anumanchipalli"
heroImage: /arxiv.jpg
linkDownload: "https://arxiv.org/pdf/2506.04226"
---

Abstract:Knowledge editing methods like MEMIT are able to make data and compute efficient updates of factual knowledge by using a single sentence to update facts and their consequences. However, what is often overlooked is a "precomputation step", which requires a one-time but significant computational cost. The authors of MEMIT originally precompute approximately 44 million hidden vectors per edited layer, which requires a forward pass over 44 million tokens. For GPT-J (6B), this precomputation step takes 36 hours on a single GPU, while it takes approximately 40 hours for Llama2-7B. Additionally, this precomputation time grows with model size. In this paper, we show that this excessive computational cost is unnecessary. Knowledge editing using MEMIT and related methods, such as ROME and EMMET, can be performed by pre-computing a very small portion of the 44 million hidden vectors. We first present the theoretical minimum number of hidden vector precomputation required for solutions of these editing methods to exist. We then empirically show that knowledge editing using these methods can be done by pre-computing significantly fewer hidden vectors. Specifically, we show that the precomputation step can be done with less than 0.3% of the originally stipulated number of hidden vectors. This saves a significant amount of precomputation time and allows users to begin editing new models within a few minutes.
