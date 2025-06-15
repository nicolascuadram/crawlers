---
title: "Eigenspectrum Analysis of Neural Networks without Aspect Ratio Bias"
description: "Machine Learning (cs.LG); Artificial Intelligence (cs.AI)"
url: "https://arxiv.org/abs/arXiv:2506.06280"
type: "paper"
pubDate: "[Submitted on 6 Jun 2025]"
created_at: "2025-06-09 16:54:24.822769"
log_id: 57
sourcename: arXiv CS
author: "Authors:Yuanzhe Hu, Kinshuk Goel, Vlad Killiakov, Yaoqing Yang"
heroImage: /arxiv.jpg
linkDownload: "https://arxiv.org/pdf/2506.06280"
---

Abstract:Diagnosing deep neural networks (DNNs) through the eigenspectrum of weight matrices has been an active area of research in recent years. At a high level, eigenspectrum analysis of DNNs involves measuring the heavytailness of the empirical spectral densities (ESD) of weight matrices. It provides insight into how well a model is trained and can guide decisions on assigning better layer-wise training hyperparameters. In this paper, we address a challenge associated with such eigenspectrum methods: the impact of the aspect ratio of weight matrices on estimated heavytailness metrics. We demonstrate that matrices of varying sizes (and aspect ratios) introduce a non-negligible bias in estimating heavytailness metrics, leading to inaccurate model diagnosis and layer-wise hyperparameter assignment. To overcome this challenge, we propose FARMS (Fixed-Aspect-Ratio Matrix Subsampling), a method that normalizes the weight matrices by subsampling submatrices with a fixed aspect ratio. Instead of measuring the heavytailness of the original ESD, we measure the average ESD of these subsampled submatrices. We show that measuring the heavytailness of these submatrices with the fixed aspect ratio can effectively mitigate the aspect ratio bias. We validate our approach across various optimization techniques and application domains that involve eigenspectrum analysis of weights, including image classification in computer vision (CV) models, scientific machine learning (SciML) model training, and large language model (LLM) pruning. Our results show that despite its simplicity, FARMS uniformly improves the accuracy of eigenspectrum analysis while enabling more effective layer-wise hyperparameter assignment in these application domains. In one of the LLM pruning experiments, FARMS reduces the perplexity of the LLaMA-7B model by 17.3% when compared with the state-of-the-art method.
