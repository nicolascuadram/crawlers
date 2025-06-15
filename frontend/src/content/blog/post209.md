---
title: "Differential Information: An Information-Theoretic Perspective on Preference Optimization"
description: "Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)"
url: "https://arxiv.org/abs/arXiv:2505.23761"
type: "paper"
pubDate: "[Submitted on 29 May 2025]"
created_at: "2025-05-31 09:06:40.094566"
log_id: 39
sourcename: arXiv CS
author: Authors:Yunjae Won, Hyunji Lee, Hyeonbin Hwang, Minjoon Seo
heroImage: /arxiv.jpg
linkDownload: "https://arxiv.org/pdf/2505.23761"
---

Abstract:Direct Preference Optimization (DPO) has become a standard technique for aligning language models with human preferences in a supervised manner. Despite its empirical success, the theoretical justification behind its log-ratio reward parameterization remains incomplete. In this work, we address this gap by utilizing the Differential Information Distribution (DID): a distribution over token sequences that captures the information gained during policy updates. First, we show that when preference labels encode the differential information required to transform a reference policy into a target policy, the log-ratio reward in DPO emerges as the uniquely optimal form for learning the target policy via preference optimization. This result naturally yields a closed-form expression for the optimal sampling distribution over rejected responses. Second, we find that the condition for preferences to encode differential information is fundamentally linked to an implicit assumption regarding log-margin ordered policies-an inductive bias widely used in preference optimization yet previously unrecognized. Finally, by analyzing the entropy of the DID, we characterize how learning low-entropy differential information reinforces the policy distribution, while high-entropy differential information induces a smoothing effect, which explains the log-likelihood displacement phenomenon. We validate our theoretical findings in synthetic experiments and extend them to real-world instruction-following datasets. Our results suggest that learning high-entropy differential information is crucial for general instruction-following, while learning low-entropy differential information benefits knowledge-intensive question answering. Overall, our work presents a unifying perspective on the DPO objective, the structure of preference data, and resulting policy behaviors through the lens of differential information.
