---
title: "Potential failures of physics-informed machine learning in traffic flow modeling: theoretical and experimental analysis"
description: "Machine Learning (cs.LG); Computational Physics (physics.comp-ph)"
url: "https://arxiv.org/abs/arXiv:2505.11491"
type: "paper"
pubDate: "pendiente"
created_at: "2025-05-19 16:02:22.715847"
log_id: 23
sourcename: arXiv CS
author: pendiente
heroImage: /arxiv.jpg
linkDownload: "pendiente"
---

Abstract:This study critically examines the performance of physics-informed machine learning (PIML) approaches for traffic flow modeling, defining the failure of a PIML model as the scenario where it underperforms both its purely data-driven and purely physics-based counterparts. We analyze the loss landscape by perturbing trained models along the principal eigenvectors of the Hessian matrix and evaluating corresponding loss values. Our results suggest that physics residuals in PIML do not inherently hinder optimization, contrary to a commonly assumed failure cause. Instead, successful parameter updates require both ML and physics gradients to form acute angles with the quasi-true gradient and lie within a conical region. Given inaccuracies in both the physics models and the training data, satisfying this condition is often difficult. Experiments reveal that physical residuals can degrade the performance of LWR- and ARZ-based PIML models, especially under highly physics-driven settings. Moreover, sparse sampling and the use of temporally averaged traffic data can produce misleadingly small physics residuals that fail to capture actual physical dynamics, contributing to model failure. We also identify the Courant-Friedrichs-Lewy (CFL) condition as a key indicator of dataset suitability for PIML, where successful applications consistently adhere to this criterion. Lastly, we observe that higher-order models like ARZ tend to have larger error lower bounds than lower-order models like LWR, which is consistent with the experimental findings of existing studies.
