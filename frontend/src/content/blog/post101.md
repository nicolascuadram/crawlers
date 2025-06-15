---
title: "Principled Approaches for Extending Neural Architectures to Function Spaces for Operator Learning"
description: "Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Functional Analysis (math.FA); Numerical Analysis (math.NA)"
url: "https://arxiv.org/abs/arXiv:2506.10973"
type: "paper"
pubDate: "[Submitted on 12 Jun 2025]"
created_at: "2025-06-13 13:31:44.378180"
log_id: 13
sourcename: arXiv CS
author: "Authors:Julius Berner, Miguel Liu-Schiaffini, Jean Kossaifi, Valentin Duruisseaux, Boris Bonev, Kamyar Azizzadenesheli, Anima Anandkumar"
heroImage: /arxiv.jpg
linkDownload: "https://arxiv.org/pdf/2506.10973"
---

Abstract:A wide range of scientific problems, such as those described by continuous-time dynamical systems and partial differential equations (PDEs), are naturally formulated on function spaces. While function spaces are typically infinite-dimensional, deep learning has predominantly advanced through applications in computer vision and natural language processing that focus on mappings between finite-dimensional spaces. Such fundamental disparities in the nature of the data have limited neural networks from achieving a comparable level of success in scientific applications as seen in other fields. Neural operators are a principled way to generalize neural networks to mappings between function spaces, offering a pathway to replicate deep learning's transformative impact on scientific problems. For instance, neural operators can learn solution operators for entire classes of PDEs, e.g., physical systems with different boundary conditions, coefficient functions, and geometries. A key factor in deep learning's success has been the careful engineering of neural architectures through extensive empirical testing. Translating these neural architectures into neural operators allows operator learning to enjoy these same empirical optimizations. However, prior neural operator architectures have often been introduced as standalone models, not directly derived as extensions of existing neural network architectures. In this paper, we identify and distill the key principles for constructing practical implementations of mappings between infinite-dimensional function spaces. Using these principles, we propose a recipe for converting several popular neural architectures into neural operators with minimal modifications. This paper aims to guide practitioners through this process and details the steps to make neural operators work in practice. Our code can be found at this https URL
