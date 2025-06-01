---
title: "Sketch Down the FLOPs: Towards Efficient Networks for Human Sketch"
description: "Computer Vision and Pattern Recognition (cs.CV)"
url: "https://arxiv.org/abs/arXiv:2505.23763"
type: "paper"
pubDate: "[Submitted on 29 May 2025]"
created_at: "2025-05-31 09:06:40.094566"
log_id: 39
sourcename: arXiv CS
author: Authors:Aneeshan Sain, Subhajit Maity, Pinaki Nath Chowdhury, Subhadeep Koley, Ayan Kumar Bhunia, Yi-Zhe Song
heroImage: /arxiv.jpg
linkDownload: "https://arxiv.org/pdf/2505.23763"
---

Abstract:As sketch research has collectively matured over time, its adaptation for at-mass commercialisation emerges on the immediate horizon. Despite an already mature research endeavour for photos, there is no research on the efficient inference specifically designed for sketch data. In this paper, we first demonstrate existing state-of-the-art efficient light-weight models designed for photos do not work on sketches. We then propose two sketch-specific components which work in a plug-n-play manner on any photo efficient network to adapt them to work on sketch data. We specifically chose fine-grained sketch-based image retrieval (FG-SBIR) as a demonstrator as the most recognised sketch problem with immediate commercial value. Technically speaking, we first propose a cross-modal knowledge distillation network to transfer existing photo efficient networks to be compatible with sketch, which brings down number of FLOPs and model parameters by 97.96% percent and 84.89% respectively. We then exploit the abstract trait of sketch to introduce a RL-based canvas selector that dynamically adjusts to the abstraction level which further cuts down number of FLOPs by two thirds. The end result is an overall reduction of 99.37% of FLOPs (from 40.18G to 0.254G) when compared with a full network, while retaining the accuracy (33.03% vs 32.77%) -- finally making an efficient network for the sparse sketch data that exhibit even fewer FLOPs than the best photo counterpart.
