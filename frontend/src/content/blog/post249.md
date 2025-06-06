---
title: "Object-centric 3D Motion Field for Robot Learning from Human Videos"
description: "Robotics (cs.RO); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV); Machine Learning (cs.LG); Systems and Control (eess.SY)"
url: "https://arxiv.org/abs/arXiv:2506.04227"
type: "paper"
pubDate: "[Submitted on 4 Jun 2025]"
created_at: "2025-06-05 21:15:40.028138"
log_id: 51
sourcename: arXiv CS
author: "Authors:Zhao-Heng Yin, Sherry Yang, Pieter Abbeel"
heroImage: /arxiv.jpg
linkDownload: "https://arxiv.org/pdf/2506.04227"
---

Abstract:Learning robot control policies from human videos is a promising direction for scaling up robot learning. However, how to extract action knowledge (or action representations) from videos for policy learning remains a key challenge. Existing action representations such as video frames, pixelflow, and pointcloud flow have inherent limitations such as modeling complexity or loss of information. In this paper, we propose to use object-centric 3D motion field to represent actions for robot learning from human videos, and present a novel framework for extracting this representation from videos for zero-shot control. We introduce two novel components in its implementation. First, a novel training pipeline for training a ''denoising'' 3D motion field estimator to extract fine object 3D motions from human videos with noisy depth robustly. Second, a dense object-centric 3D motion field prediction architecture that favors both cross-embodiment transfer and policy generalization to background. We evaluate the system in real world setups. Experiments show that our method reduces 3D motion estimation error by over 50% compared to the latest method, achieve 55% average success rate in diverse tasks where prior approaches fail~($\lesssim 10$\%), and can even acquire fine-grained manipulation skills like insertion.
