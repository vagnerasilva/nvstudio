from sagemaker.processing import Processor
from sagemaker.processing import ProcessingInput
from sagemaker.processing import ProcessingOutput

""" ##### Parametros Processor #####
        role: str = None,
        image_uri: Union[str, PipelineVariable] = None,
        instance_count: Union[int, PipelineVariable] = None,
        instance_type: Union[str, PipelineVariable] = None,
        entrypoint: Optional[List[Union[str, PipelineVariable]]] = None,
        volume_size_in_gb: Union[int, PipelineVariable] = 30,
        volume_kms_key: Optional[Union[str, PipelineVariable]] = None,
        output_kms_key: Optional[Union[str, PipelineVariable]] = None,
        max_runtime_in_seconds: Optional[Union[int, PipelineVariable]] = None,
        base_job_name: Optional[str] = None,
        sagemaker_session: Optional[Session] = None,
        env: Optional[Dict[str, Union[str, PipelineVariable]]] = None,
        tags: Optional[Tags] = None,
        network_config: Optional[NetworkConfig] = None,
    ##### Parametros Processor #####
"""

processor = Processor(
            role=role,      
            image_uri='<your_ecr_image_uri>',
            instance_count=1,
            instance_type="ml.m5.xlarge"
        )

"""##### Parametros run #####
        self,
        inputs: Optional[List["ProcessingInput"]] = None,
        outputs: Optional[List["ProcessingOutput"]] = None,
        arguments: Optional[List[Union[str, PipelineVariable]]] = None,
        wait: bool = True,
        logs: bool = True,
        job_name: Optional[str] = None,
        experiment_config: Optional[Dict[str, str]] = None,
        kms_key: Optional[str] = None,
    ##### Parametros run #####
"""




processor.run(
               inputs=[
                    ProcessingInput(
                        source='<s3_uri or local path>',
                        destination='/opt/ml/processing/input_data')
                ],




                outputs=[
                    ProcessingOutput(
                        source='/opt/ml/processing/processed_data',
                        destination='<s3_uri>'
                        )
                ],
                
            )
                """ ##### Parametros ProcessingInput #####
                        source: Optional[Union[str, PipelineVariable]] = None,
                        destination: Optional[Union[str, PipelineVariable]] = None,
                        input_name: Optional[Union[str, PipelineVariable]] = None,
                        s3_data_type: Union[str, PipelineVariable] = "S3Prefix",
                        s3_input_mode: Union[str, PipelineVariable] = "File",
                        s3_data_distribution_type: Union[str, PipelineVariable] = "FullyReplicated",
                        s3_compression_type: Union[str, PipelineVariable] = "None",
                        s3_input: Optional[S3Input] = None,
                        dataset_definition: Optional[DatasetDefinition] = None,
                        app_managed: Union[bool, PipelineVariable] = False,
                """



                        """ ##### Parametros ProcessingOutput #####
                        source: Optional[Union[str, PipelineVariable]] = None,
                        destination: Optional[Union[str, PipelineVariable]] = None,
                        output_name: Optional[Union[str, PipelineVariable]] = None,
                        s3_upload_mode: Union[str, PipelineVariable] = "EndOfJob",
                        app_managed: Union[bool, PipelineVariable] = False,
                        feature_store_output: Optional["FeatureStoreOutput"] = None,
                        """
