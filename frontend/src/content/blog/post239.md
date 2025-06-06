---
title: "AdaHuman: Animatable Detailed 3D Human Generation with Compositional Multiview Diffusion"
description: "Computer Vision and Pattern Recognition (cs.CV)"
url: "https://arxiv.org/abs/arXiv:2505.24877"
type: "paper"
pubDate: "[Submitted on 30 May 2025]"
created_at: "2025-06-02 14:41:35.057864"
log_id: 42
sourcename: arXiv CS
author: "Authors:Yangyi Huang, Ye Yuan, Xueting Li, Jan Kautz, Umar Iqbal"
heroImage: /arxiv.jpg
linkDownload: "https://arxiv.org/pdf/2505.24877"
---

Abstract:Existing methods for image-to-3D avatar generation struggle to produce highly detailed, animation-ready avatars suitable for real-world applications. We introduce AdaHuman, a novel framework that generates high-fidelity animatable 3D avatars from a single in-the-wild image. AdaHuman incorporates two key innovations: (1) A pose-conditioned 3D joint diffusion model that synthesizes consistent multi-view images in arbitrary poses alongside corresponding 3D Gaussian Splats (3DGS) reconstruction at each diffusion step; (2) A compositional 3DGS refinement module that enhances the details of local body parts through image-to-image refinement and seamlessly integrates them using a novel crop-aware camera ray map, producing a cohesive detailed 3D avatar. These components allow AdaHuman to generate highly realistic standardized A-pose avatars with minimal self-occlusion, enabling rigging and animation with any input motion. Extensive evaluation on public benchmarks and in-the-wild images demonstrates that AdaHuman significantly outperforms state-of-the-art methods in both avatar reconstruction and reposing. Code and models will be publicly available for research purposes.
