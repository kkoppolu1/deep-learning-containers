import os

import pytest

from test.test_utils import CONTAINER_TESTS_PREFIX
from test.test_utils.ec2 import execute_ec2_training_test, get_ec2_instance_type


MX_STANDALONE_CMD = os.path.join(CONTAINER_TESTS_PREFIX, "testMXNetStandalone")
MX_MNIST_CMD = os.path.join(CONTAINER_TESTS_PREFIX, "testMXNet")
MX_DGL_CMD = os.path.join(CONTAINER_TESTS_PREFIX, "dgl_tests", "testMXNetDGL")
MX_NLP_CMD = os.path.join(CONTAINER_TESTS_PREFIX, "gluonnlp_tests", "testNLP")
MX_HVD_CMD = os.path.join(CONTAINER_TESTS_PREFIX, "testMXNetHVD")
MX_KERAS_CMD = os.path.join(CONTAINER_TESTS_PREFIX, "testKerasMXNet")
MX_TELEMETRY_CMD = os.path.join(CONTAINER_TESTS_PREFIX, "test_mx_dlc_telemetry_test")

MX_EC2_GPU_INSTANCE_TYPE = get_ec2_instance_type(default="g3.8xlarge", processor="gpu")
MX_EC2_CPU_INSTANCE_TYPE = get_ec2_instance_type(default="c5.4xlarge", processor="cpu")


@pytest.mark.integration("mxnet_sanity_test")
@pytest.mark.model("N/A")
@pytest.mark.parametrize("ec2_instance_type", MX_EC2_GPU_INSTANCE_TYPE, indirect=True)
def test_mxnet_standalone_gpu(mxnet_training, ec2_connection, gpu_only):
    execute_ec2_training_test(ec2_connection, mxnet_training, MX_STANDALONE_CMD)


@pytest.mark.integration("mxnet_sanity_test")
@pytest.mark.model("N/A")
@pytest.mark.parametrize("ec2_instance_type", MX_EC2_CPU_INSTANCE_TYPE, indirect=True)
def test_mxnet_standalone_cpu(mxnet_training, ec2_connection, cpu_only):
    execute_ec2_training_test(ec2_connection, mxnet_training, MX_STANDALONE_CMD)


@pytest.mark.model("mnist")
@pytest.mark.parametrize("ec2_instance_type", MX_EC2_GPU_INSTANCE_TYPE, indirect=True)
def test_mxnet_train_mnist_gpu(mxnet_training, ec2_connection, gpu_only):
    execute_ec2_training_test(ec2_connection, mxnet_training, MX_MNIST_CMD)


@pytest.mark.model("mnist")
@pytest.mark.parametrize("ec2_instance_type", MX_EC2_CPU_INSTANCE_TYPE, indirect=True)
def test_mxnet_train_mnist_cpu(mxnet_training, ec2_connection, cpu_only):
    execute_ec2_training_test(ec2_connection, mxnet_training, MX_MNIST_CMD)


@pytest.mark.integration("keras")
@pytest.mark.model("resnet")
@pytest.mark.parametrize("ec2_instance_type", MX_EC2_GPU_INSTANCE_TYPE, indirect=True)
def test_mxnet_keras_gpu(mxnet_training, ec2_connection, gpu_only):
    execute_ec2_training_test(ec2_connection, mxnet_training, MX_KERAS_CMD)


@pytest.mark.integration("keras")
@pytest.mark.model("resnet")
@pytest.mark.parametrize("ec2_instance_type", MX_EC2_CPU_INSTANCE_TYPE, indirect=True)
def test_mxnet_keras_cpu(mxnet_training, ec2_connection, cpu_only):
    execute_ec2_training_test(ec2_connection, mxnet_training, MX_KERAS_CMD)


@pytest.mark.integration("dgl")
@pytest.mark.model("gcn")
@pytest.mark.parametrize("ec2_instance_type", MX_EC2_GPU_INSTANCE_TYPE, indirect=True)
def test_mxnet_train_dgl_gpu(mxnet_training, ec2_connection, gpu_only, py3_only):
    if "cu110" in mxnet_training:
        pytest.skip("Skipping dgl tests on cuda 11.0 until available")
    execute_ec2_training_test(ec2_connection, mxnet_training, MX_DGL_CMD)


@pytest.mark.integration("dgl")
@pytest.mark.model("gcn")
@pytest.mark.parametrize("ec2_instance_type", MX_EC2_CPU_INSTANCE_TYPE, indirect=True)
def test_mxnet_train_dgl_cpu(mxnet_training, ec2_connection, cpu_only, py3_only):
    execute_ec2_training_test(ec2_connection, mxnet_training, MX_DGL_CMD)


@pytest.mark.integration("gluonnlp")
@pytest.mark.model("textCNN")
@pytest.mark.parametrize("ec2_instance_type", MX_EC2_GPU_INSTANCE_TYPE, indirect=True)
def test_mxnet_train_nlp_gpu(mxnet_training, ec2_connection, gpu_only, py3_only):
    execute_ec2_training_test(ec2_connection, mxnet_training, MX_NLP_CMD)


@pytest.mark.integration("gluonnlp")
@pytest.mark.model("textCNN")
@pytest.mark.parametrize("ec2_instance_type", MX_EC2_CPU_INSTANCE_TYPE, indirect=True)
def test_mxnet_train_nlp_cpu(mxnet_training, ec2_connection, cpu_only, py3_only):
    execute_ec2_training_test(ec2_connection, mxnet_training, MX_NLP_CMD)


@pytest.mark.integration("horovod")
@pytest.mark.model("AlexNet")
@pytest.mark.parametrize("ec2_instance_type", MX_EC2_GPU_INSTANCE_TYPE, indirect=True)
def test_mxnet_with_horovod_gpu(mxnet_training, ec2_connection, gpu_only):
    execute_ec2_training_test(ec2_connection, mxnet_training, MX_HVD_CMD)


@pytest.mark.integration("horovod")
@pytest.mark.model("AlexNet")
@pytest.mark.parametrize("ec2_instance_type", MX_EC2_CPU_INSTANCE_TYPE, indirect=True)
def test_mxnet_with_horovod_cpu(mxnet_training, ec2_connection, cpu_only):
    execute_ec2_training_test(ec2_connection, mxnet_training, MX_HVD_CMD)


@pytest.mark.flaky(reruns=3)
@pytest.mark.integration("telemetry")
@pytest.mark.model("N/A")
@pytest.mark.parametrize("ec2_instance_type", ["p2.xlarge"], indirect=True)
def test_mxnet_telemetry_gpu(mxnet_training, ec2_connection, gpu_only):
    execute_ec2_training_test(ec2_connection, mxnet_training, MX_TELEMETRY_CMD)


@pytest.mark.flaky(reruns=3)
@pytest.mark.integration("telemetry")
@pytest.mark.model("N/A")
@pytest.mark.parametrize("ec2_instance_type", ["c5.4xlarge"], indirect=True)
def test_mxnet_telemetry_cpu(mxnet_training, ec2_connection, cpu_only):
    execute_ec2_training_test(ec2_connection, mxnet_training, MX_TELEMETRY_CMD)
