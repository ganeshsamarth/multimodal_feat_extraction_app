# Visual Feature Outputs - Weapons + Objects
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2






class VisualFeatures:

    def __init__(self, PERSONAL_TOKEN = '1497c2be9d2447dcb6a21c94b382515a'):

         
        channel = ClarifaiChannel.get_grpc_channel()
        self.stub = service_pb2_grpc.V2Stub(channel)

        self.metadata = (('authorization', 'Key ' + YOUR_PERSONAL_TOKEN),)


    def weapon_detection(self, frame):
        # frame is a numpy array
        weapons_dict = {}
        success, encoded_image = cv2.imencode('.png', frame)
        file_bytes = encoded_image.tobytes()

        userDataObject = resources_pb2.UserAppIDSet(user_id='clarifai', app_id='main')

        post_model_outputs_response = self.stub.PostModelOutputs(
            service_pb2.PostModelOutputsRequest(
                user_app_id=userDataObject,
                model_id='weapon-detection',
                inputs=[
                    resources_pb2.Input(
                        data=resources_pb2.Data(
                            image = resources_pb2.Video(base64=file_bytes)
                        )
                    )
                ]
            ),
            metadata=self.metadata
        )

        output = post_model_outputs_response.outputs[0]

        
        threshold = 0.8
        for regions in output.data.regions:
        # print(regions.data.concepts)
        if regions.value > threshold:
            if regions.data.concepts[0].name in weapons_dict:
            weapons_dict[regions.data.concepts[0].name].append(regions.value)
            else:
            weapons_dict[regions.data.concepts[0].name] = [regions.value]
        

        return weapons_dict



        