# Copyright (c) Meta Platforms, Inc. and affiliates
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from seamless_communication.streaming.agents.online_feature_extractor import (
    OnlineFeatureExtractorAgent,
)
from seamless_communication.streaming.agents.unity_pipeline import UnitYAgentPipeline
from simuleval.utils import entrypoint


@entrypoint
class MonotonicM4TS2TSPMAgent(UnitYAgentPipeline):
    pipeline = [OnlineFeatureExtractorAgent]
