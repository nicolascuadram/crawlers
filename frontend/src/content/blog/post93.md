---
title: "Rethinking Losses for Diffusion Bridge Samplers"
description: "Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Machine Learning (stat.ML)"
url: "https://arxiv.org/abs/arXiv:2506.10982"
type: "paper"
pubDate: "[Submitted on 12 Jun 2025]"
created_at: "2025-06-13 13:31:44.378180"
log_id: 13
sourcename: arXiv CS
author: "Authors:Sebastian Sanokowski, Lukas Gruber, Christoph Bartmann, Sepp Hochreiter, Sebastian Lehner"
heroImage: /arxiv.jpg
linkDownload: "https://arxiv.org/pdf/2506.10982"
---

Abstract:Diffusion bridges are a promising class of deep-learning methods for sampling from unnormalized distributions. Recent works show that the Log Variance (LV) loss consistently outperforms the reverse Kullback-Leibler (rKL) loss when using the reparametrization trick to compute rKL-gradients. While the on-policy LV loss yields identical gradients to the rKL loss when combined with the log-derivative trick for diffusion samplers with non-learnable forward processes, this equivalence does not hold for diffusion bridges or when diffusion coefficients are learned. Based on this insight we argue that for diffusion bridges the LV loss does not represent an optimization objective that can be motivated like the rKL loss via the data processing inequality. Our analysis shows that employing the rKL loss with the log-derivative trick (rKL-LD) does not only avoid these conceptual problems but also consistently outperforms the LV loss. Experimental results with different types of diffusion bridges on challenging benchmarks show that samplers trained with the rKL-LD loss achieve better performance. From a practical perspective we find that rKL-LD requires significantly less hyperparameter optimization and yields more stable training behavior.
