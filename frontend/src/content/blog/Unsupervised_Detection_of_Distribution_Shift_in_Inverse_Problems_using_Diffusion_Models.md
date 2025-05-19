---
title: "Unsupervised Detection of Distribution Shift in Inverse Problems using Diffusion Models"
description: "Computer Vision and Pattern Recognition (cs.CV)"
url: "https://arxiv.org/abs/arXiv:2505.11482"
type: "paper"
pubDate: "pendiente"
created_at: "2025-05-19 16:02:22.715847"
log_id: 23
sourcename: arXiv CS
author: pendiente
heroImage: /arxiv.jpg
linkDownload: "pendiente"
---

Abstract:Diffusion models are widely used as priors in imaging inverse problems. However, their performance often degrades under distribution shifts between the training and test-time images. Existing methods for identifying and quantifying distribution shifts typically require access to clean test images, which are almost never available while solving inverse problems (at test time). We propose a fully unsupervised metric for estimating distribution shifts using only indirect (corrupted) measurements and score functions from diffusion models trained on different datasets. We theoretically show that this metric estimates the KL divergence between the training and test image distributions. Empirically, we show that our score-based metric, using only corrupted measurements, closely approximates the KL divergence computed from clean images. Motivated by this result, we show that aligning the out-of-distribution score with the in-distribution score -- using only corrupted measurements -- reduces the KL divergence and leads to improved reconstruction quality across multiple inverse problems.
