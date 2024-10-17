# Copyright (c) MONAI Consortium
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

from monailabel.interfaces.datastore import Datastore
from monailabel.interfaces.tasks.strategy import Strategy

logger = logging.getLogger(__name__)


class User_Based(Strategy):
    """
    Consider implementing a random strategy for active learning
    """

    def __init__(self):
        super().__init__("User Based Strategy")

    def __call__(self, request, datastore: Datastore):
        label_tag = request.get("label_tag")
        labels = request.get("labels")
        images = datastore.get_unlabeled_images(label_tag, labels)

        eligible_images = []

        for img in images:
            # Checking if an image has been tagged by a user or not yet
            if datastore.get_image_info(img).get("strategy") == None :
                eligible_images.append(img)
            # Checking, in the case a user tag is found, if it corresponds to the one of current user
            elif datastore.get_image_info(img).get("strategy") != None:

                if datastore.get_image_info(img).get("strategy").get("user_based") != None:

                    if datastore.get_image_info(img).get("strategy").get("user_based").get("client_id") != None:

                        if datastore.get_image_info(img).get("strategy").get("user_based").get("client_id") == request.get("client_id"):
                            eligible_images.append(img)
                        


        if not len(eligible_images):
            return None

        eligible_images.sort()
        print("Eligible images: ", eligible_images)
        image = eligible_images[0]
        logger.info(f"First: Selected Image: {image}")
        return {"id": image}
