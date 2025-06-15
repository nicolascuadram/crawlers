---
title: "Agronomy, Vol. 15, Pages 1396: FRPNet: A Lightweight Multi-Altitude Field Rice Panicle Detection and Counting Network Based on Unmanned Aerial Vehicle Images"
description: ""
url: "https://www.mdpi.com/2073-4395/15/6/1396"
type: "paper"
pubDate: "2025-06-05"
created_at: "2025-06-05 21:21:29.899135"
log_id: 56
sourcename: MDPI
author: "\"Yuheng Guo\",\"Wei Zhan\",\"Zhiliang Zhang\",\"Yu Zhang\",\"Hongshen Guo\""
heroImage: /mdpi.jpg
linkDownload: "https://www.mdpi.com/2073-4395/15/6/1396"
---

Rice panicle detection is a key technology for improving rice yield and agricultural management levels. Traditional manual counting methods are labor-intensive and inefficient, making them unsuitable for large-scale farmlands. This paper proposes FRPNet, a novel lightweight convolutional neural network optimized for multi-altitude rice panicle detection in UAV images. The architecture integrates three core innovations: a CSP-ScConv backbone with self-calibrating convolutions for efficient multi-scale feature extraction; a Feature Pyramid Shared Convolution (FPSC) module that replaces pooling with multi-branch dilated convolutions to preserve fine-grained spatial information; and a Dynamic Bidirectional Feature Pyramid Network (DynamicBiFPN) employing input-adaptive kernels to optimize cross-scale feature fusion. The model was trained and evaluated on the open-access Dense Rice Panicle Detection (DRPD) dataset, which comprises UAV images captured at 7 m, 12 m, and 20 m altitudes. Experimental results demonstrate that our method significantly outperforms existing advanced models, achieving an AP50 of 0.8931 and an F2 score of 0.8377 on the test set. While ensuring model accuracy, the parameters of the proposed model decreased by 42.87% and the GFLOPs by 48.95% compared to Panicle-AI. Grad-CAM visualizations reveal that FRPNet exhibits superior background noise suppression in 20 m altitude images compared to mainstream models. This work establishes an accuracy-efficiency balanced solution for UAV-based field phenotyping.
