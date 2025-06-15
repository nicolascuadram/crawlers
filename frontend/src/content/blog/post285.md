---
title: "AdvSumm: Adversarial Training for Bias Mitigation in Text Summarization"
description: "Computation and Language (cs.CL)"
url: "https://arxiv.org/abs/arXiv:2506.06273"
type: "paper"
pubDate: "[Submitted on 6 Jun 2025]"
created_at: "2025-06-09 16:54:24.822769"
log_id: 57
sourcename: arXiv CS
author: "Authors:Mukur Gupta, Nikhil Reddy Varimalla, Nicholas Deas, Melanie Subbiah, Kathleen McKeown"
heroImage: /arxiv.jpg
linkDownload: "https://arxiv.org/pdf/2506.06273"
---

Abstract:Large Language Models (LLMs) have achieved impressive performance in text summarization and are increasingly deployed in real-world applications. However, these systems often inherit associative and framing biases from pre-training data, leading to inappropriate or unfair outputs in downstream tasks. In this work, we present AdvSumm (Adversarial Summarization), a domain-agnostic training framework designed to mitigate bias in text summarization through improved generalization. Inspired by adversarial robustness, AdvSumm introduces a novel Perturber component that applies gradient-guided perturbations at the embedding level of Sequence-to-Sequence models, enhancing the model's robustness to input variations. We empirically demonstrate that AdvSumm effectively reduces different types of bias in summarization-specifically, name-nationality bias and political framing bias-without compromising summarization quality. Compared to standard transformers and data augmentation techniques like back-translation, AdvSumm achieves stronger bias mitigation performance across benchmark datasets.
