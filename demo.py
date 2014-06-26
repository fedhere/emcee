#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import numpy as np
import matplotlib.pyplot as pl

from emcee import proposals
from emcee.sampler import SimpleSampler

np.random.seed(1234)


def lnprior(p):
    return 0.0


def lnlike(p):
    return -0.5 * np.sum(p**2)


ndim = 10
sampler = SimpleSampler(lnprior, lnlike, proposals.StretchProposal())
# sampler = SimpleSampler(lnprior, lnlike, proposals.GaussianProposal(ndim, 1.0))
p0 = 1.0 + 0.1 * np.random.randn(100, ndim)

for i, state in enumerate(sampler.sample(p0, nstep=5000)):
    pass

print(sampler.acceptance_fraction)
print(sampler.chain.shape)
print(np.mean(sampler.chain, axis=(0, 1)))
print(np.std(sampler.chain, axis=(0, 1)))

pl.hist(sampler.chain[:, :, 0].flatten(), 50, histtype="step", color="k",
        normed=True)
x = np.linspace(-6, 6, 5000)
pl.plot(x, np.exp(-0.5 * x**2) / np.sqrt(2*np.pi))

pl.savefig("dude.png")

pl.clf()
pl.plot(sampler.chain[:, :, 0])
pl.savefig("dude2.png")