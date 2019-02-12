# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from .week_details_py3 import WeekDetails
    from .day_details_py3 import DayDetails
    from .hour_details_py3 import HourDetails
    from .notification_settings_py3 import NotificationSettings
    from .schedule_py3 import Schedule
    from .applicable_schedule_py3 import ApplicableSchedule
    from .week_details_fragment_py3 import WeekDetailsFragment
    from .day_details_fragment_py3 import DayDetailsFragment
    from .hour_details_fragment_py3 import HourDetailsFragment
    from .notification_settings_fragment_py3 import NotificationSettingsFragment
    from .schedule_fragment_py3 import ScheduleFragment
    from .applicable_schedule_fragment_py3 import ApplicableScheduleFragment
    from .artifact_parameter_properties_py3 import ArtifactParameterProperties
    from .artifact_install_properties_py3 import ArtifactInstallProperties
    from .apply_artifacts_request_py3 import ApplyArtifactsRequest
    from .parameters_value_file_info_py3 import ParametersValueFileInfo
    from .arm_template_py3 import ArmTemplate
    from .arm_template_info_py3 import ArmTemplateInfo
    from .arm_template_parameter_properties_py3 import ArmTemplateParameterProperties
    from .arm_template_parameter_properties_fragment_py3 import ArmTemplateParameterPropertiesFragment
    from .artifact_py3 import Artifact
    from .artifact_deployment_status_properties_py3 import ArtifactDeploymentStatusProperties
    from .artifact_deployment_status_properties_fragment_py3 import ArtifactDeploymentStatusPropertiesFragment
    from .artifact_parameter_properties_fragment_py3 import ArtifactParameterPropertiesFragment
    from .artifact_install_properties_fragment_py3 import ArtifactInstallPropertiesFragment
    from .artifact_source_py3 import ArtifactSource
    from .artifact_source_fragment_py3 import ArtifactSourceFragment
    from .attach_disk_properties_py3 import AttachDiskProperties
    from .attach_new_data_disk_options_py3 import AttachNewDataDiskOptions
    from .attach_new_data_disk_options_fragment_py3 import AttachNewDataDiskOptionsFragment
    from .bulk_creation_parameters_py3 import BulkCreationParameters
    from .bulk_creation_parameters_fragment_py3 import BulkCreationParametersFragment
    from .compute_data_disk_py3 import ComputeDataDisk
    from .compute_data_disk_fragment_py3 import ComputeDataDiskFragment
    from .compute_vm_instance_view_status_py3 import ComputeVmInstanceViewStatus
    from .compute_vm_instance_view_status_fragment_py3 import ComputeVmInstanceViewStatusFragment
    from .compute_vm_properties_py3 import ComputeVmProperties
    from .compute_vm_properties_fragment_py3 import ComputeVmPropertiesFragment
    from .percentage_cost_threshold_properties_py3 import PercentageCostThresholdProperties
    from .cost_threshold_properties_py3 import CostThresholdProperties
    from .windows_os_info_py3 import WindowsOsInfo
    from .linux_os_info_py3 import LinuxOsInfo
    from .custom_image_properties_from_vm_py3 import CustomImagePropertiesFromVm
    from .custom_image_properties_custom_py3 import CustomImagePropertiesCustom
    from .data_disk_storage_type_info_py3 import DataDiskStorageTypeInfo
    from .custom_image_properties_from_plan_py3 import CustomImagePropertiesFromPlan
    from .custom_image_py3 import CustomImage
    from .windows_os_info_fragment_py3 import WindowsOsInfoFragment
    from .linux_os_info_fragment_py3 import LinuxOsInfoFragment
    from .custom_image_properties_from_vm_fragment_py3 import CustomImagePropertiesFromVmFragment
    from .custom_image_properties_custom_fragment_py3 import CustomImagePropertiesCustomFragment
    from .data_disk_storage_type_info_fragment_py3 import DataDiskStorageTypeInfoFragment
    from .custom_image_properties_from_plan_fragment_py3 import CustomImagePropertiesFromPlanFragment
    from .custom_image_fragment_py3 import CustomImageFragment
    from .data_disk_properties_py3 import DataDiskProperties
    from .data_disk_properties_fragment_py3 import DataDiskPropertiesFragment
    from .detach_data_disk_properties_py3 import DetachDataDiskProperties
    from .detach_disk_properties_py3 import DetachDiskProperties
    from .disk_py3 import Disk
    from .disk_fragment_py3 import DiskFragment
    from .environment_deployment_properties_py3 import EnvironmentDeploymentProperties
    from .dtl_environment_py3 import DtlEnvironment
    from .environment_deployment_properties_fragment_py3 import EnvironmentDeploymentPropertiesFragment
    from .dtl_environment_fragment_py3 import DtlEnvironmentFragment
    from .evaluate_policies_properties_py3 import EvaluatePoliciesProperties
    from .evaluate_policies_request_py3 import EvaluatePoliciesRequest
    from .policy_violation_py3 import PolicyViolation
    from .policy_set_result_py3 import PolicySetResult
    from .evaluate_policies_response_py3 import EvaluatePoliciesResponse
    from .event_py3 import Event
    from .event_fragment_py3 import EventFragment
    from .export_resource_usage_parameters_py3 import ExportResourceUsageParameters
    from .external_subnet_py3 import ExternalSubnet
    from .external_subnet_fragment_py3 import ExternalSubnetFragment
    from .gallery_image_reference_py3 import GalleryImageReference
    from .inbound_nat_rule_py3 import InboundNatRule
    from .shared_public_ip_address_configuration_py3 import SharedPublicIpAddressConfiguration
    from .network_interface_properties_py3 import NetworkInterfaceProperties
    from .schedule_creation_parameter_py3 import ScheduleCreationParameter
    from .lab_virtual_machine_creation_parameter_py3 import LabVirtualMachineCreationParameter
    from .formula_properties_from_vm_py3 import FormulaPropertiesFromVm
    from .formula_py3 import Formula
    from .gallery_image_reference_fragment_py3 import GalleryImageReferenceFragment
    from .inbound_nat_rule_fragment_py3 import InboundNatRuleFragment
    from .shared_public_ip_address_configuration_fragment_py3 import SharedPublicIpAddressConfigurationFragment
    from .network_interface_properties_fragment_py3 import NetworkInterfacePropertiesFragment
    from .schedule_creation_parameter_fragment_py3 import ScheduleCreationParameterFragment
    from .lab_virtual_machine_creation_parameter_fragment_py3 import LabVirtualMachineCreationParameterFragment
    from .formula_properties_from_vm_fragment_py3 import FormulaPropertiesFromVmFragment
    from .formula_fragment_py3 import FormulaFragment
    from .gallery_image_py3 import GalleryImage
    from .parameter_info_py3 import ParameterInfo
    from .generate_arm_template_request_py3 import GenerateArmTemplateRequest
    from .generate_upload_uri_parameter_py3 import GenerateUploadUriParameter
    from .generate_upload_uri_response_py3 import GenerateUploadUriResponse
    from .identity_properties_py3 import IdentityProperties
    from .import_lab_virtual_machine_request_py3 import ImportLabVirtualMachineRequest
    from .lab_announcement_properties_py3 import LabAnnouncementProperties
    from .lab_support_properties_py3 import LabSupportProperties
    from .lab_py3 import Lab
    from .lab_announcement_properties_fragment_py3 import LabAnnouncementPropertiesFragment
    from .target_cost_properties_py3 import TargetCostProperties
    from .lab_cost_summary_properties_py3 import LabCostSummaryProperties
    from .lab_cost_details_properties_py3 import LabCostDetailsProperties
    from .lab_resource_cost_properties_py3 import LabResourceCostProperties
    from .lab_cost_py3 import LabCost
    from .lab_support_properties_fragment_py3 import LabSupportPropertiesFragment
    from .lab_fragment_py3 import LabFragment
    from .lab_vhd_py3 import LabVhd
    from .lab_virtual_machine_py3 import LabVirtualMachine
    from .lab_virtual_machine_fragment_py3 import LabVirtualMachineFragment
    from .notification_channel_py3 import NotificationChannel
    from .notification_channel_fragment_py3 import NotificationChannelFragment
    from .notify_parameters_py3 import NotifyParameters
    from .operation_error_py3 import OperationError
    from .operation_metadata_display_py3 import OperationMetadataDisplay
    from .operation_metadata_py3 import OperationMetadata
    from .operation_result_py3 import OperationResult
    from .policy_py3 import Policy
    from .policy_fragment_py3 import PolicyFragment
    from .port_py3 import Port
    from .port_fragment_py3 import PortFragment
    from .rdp_connection_py3 import RdpConnection
    from .resize_lab_virtual_machine_properties_py3 import ResizeLabVirtualMachineProperties
    from .resource_py3 import Resource
    from .retarget_schedule_properties_py3 import RetargetScheduleProperties
    from .secret_py3 import Secret
    from .secret_fragment_py3 import SecretFragment
    from .service_fabric_py3 import ServiceFabric
    from .service_fabric_fragment_py3 import ServiceFabricFragment
    from .service_runner_py3 import ServiceRunner
    from .shutdown_notification_content_py3 import ShutdownNotificationContent
    from .subnet_py3 import Subnet
    from .subnet_fragment_py3 import SubnetFragment
    from .subnet_shared_public_ip_address_configuration_py3 import SubnetSharedPublicIpAddressConfiguration
    from .subnet_override_py3 import SubnetOverride
    from .subnet_shared_public_ip_address_configuration_fragment_py3 import SubnetSharedPublicIpAddressConfigurationFragment
    from .subnet_override_fragment_py3 import SubnetOverrideFragment
    from .update_resource_py3 import UpdateResource
    from .user_identity_py3 import UserIdentity
    from .user_secret_store_py3 import UserSecretStore
    from .user_py3 import User
    from .user_identity_fragment_py3 import UserIdentityFragment
    from .user_secret_store_fragment_py3 import UserSecretStoreFragment
    from .user_fragment_py3 import UserFragment
    from .virtual_network_py3 import VirtualNetwork
    from .virtual_network_fragment_py3 import VirtualNetworkFragment
except (SyntaxError, ImportError):
    from .week_details import WeekDetails
    from .day_details import DayDetails
    from .hour_details import HourDetails
    from .notification_settings import NotificationSettings
    from .schedule import Schedule
    from .applicable_schedule import ApplicableSchedule
    from .week_details_fragment import WeekDetailsFragment
    from .day_details_fragment import DayDetailsFragment
    from .hour_details_fragment import HourDetailsFragment
    from .notification_settings_fragment import NotificationSettingsFragment
    from .schedule_fragment import ScheduleFragment
    from .applicable_schedule_fragment import ApplicableScheduleFragment
    from .artifact_parameter_properties import ArtifactParameterProperties
    from .artifact_install_properties import ArtifactInstallProperties
    from .apply_artifacts_request import ApplyArtifactsRequest
    from .parameters_value_file_info import ParametersValueFileInfo
    from .arm_template import ArmTemplate
    from .arm_template_info import ArmTemplateInfo
    from .arm_template_parameter_properties import ArmTemplateParameterProperties
    from .arm_template_parameter_properties_fragment import ArmTemplateParameterPropertiesFragment
    from .artifact import Artifact
    from .artifact_deployment_status_properties import ArtifactDeploymentStatusProperties
    from .artifact_deployment_status_properties_fragment import ArtifactDeploymentStatusPropertiesFragment
    from .artifact_parameter_properties_fragment import ArtifactParameterPropertiesFragment
    from .artifact_install_properties_fragment import ArtifactInstallPropertiesFragment
    from .artifact_source import ArtifactSource
    from .artifact_source_fragment import ArtifactSourceFragment
    from .attach_disk_properties import AttachDiskProperties
    from .attach_new_data_disk_options import AttachNewDataDiskOptions
    from .attach_new_data_disk_options_fragment import AttachNewDataDiskOptionsFragment
    from .bulk_creation_parameters import BulkCreationParameters
    from .bulk_creation_parameters_fragment import BulkCreationParametersFragment
    from .compute_data_disk import ComputeDataDisk
    from .compute_data_disk_fragment import ComputeDataDiskFragment
    from .compute_vm_instance_view_status import ComputeVmInstanceViewStatus
    from .compute_vm_instance_view_status_fragment import ComputeVmInstanceViewStatusFragment
    from .compute_vm_properties import ComputeVmProperties
    from .compute_vm_properties_fragment import ComputeVmPropertiesFragment
    from .percentage_cost_threshold_properties import PercentageCostThresholdProperties
    from .cost_threshold_properties import CostThresholdProperties
    from .windows_os_info import WindowsOsInfo
    from .linux_os_info import LinuxOsInfo
    from .custom_image_properties_from_vm import CustomImagePropertiesFromVm
    from .custom_image_properties_custom import CustomImagePropertiesCustom
    from .data_disk_storage_type_info import DataDiskStorageTypeInfo
    from .custom_image_properties_from_plan import CustomImagePropertiesFromPlan
    from .custom_image import CustomImage
    from .windows_os_info_fragment import WindowsOsInfoFragment
    from .linux_os_info_fragment import LinuxOsInfoFragment
    from .custom_image_properties_from_vm_fragment import CustomImagePropertiesFromVmFragment
    from .custom_image_properties_custom_fragment import CustomImagePropertiesCustomFragment
    from .data_disk_storage_type_info_fragment import DataDiskStorageTypeInfoFragment
    from .custom_image_properties_from_plan_fragment import CustomImagePropertiesFromPlanFragment
    from .custom_image_fragment import CustomImageFragment
    from .data_disk_properties import DataDiskProperties
    from .data_disk_properties_fragment import DataDiskPropertiesFragment
    from .detach_data_disk_properties import DetachDataDiskProperties
    from .detach_disk_properties import DetachDiskProperties
    from .disk import Disk
    from .disk_fragment import DiskFragment
    from .environment_deployment_properties import EnvironmentDeploymentProperties
    from .dtl_environment import DtlEnvironment
    from .environment_deployment_properties_fragment import EnvironmentDeploymentPropertiesFragment
    from .dtl_environment_fragment import DtlEnvironmentFragment
    from .evaluate_policies_properties import EvaluatePoliciesProperties
    from .evaluate_policies_request import EvaluatePoliciesRequest
    from .policy_violation import PolicyViolation
    from .policy_set_result import PolicySetResult
    from .evaluate_policies_response import EvaluatePoliciesResponse
    from .event import Event
    from .event_fragment import EventFragment
    from .export_resource_usage_parameters import ExportResourceUsageParameters
    from .external_subnet import ExternalSubnet
    from .external_subnet_fragment import ExternalSubnetFragment
    from .gallery_image_reference import GalleryImageReference
    from .inbound_nat_rule import InboundNatRule
    from .shared_public_ip_address_configuration import SharedPublicIpAddressConfiguration
    from .network_interface_properties import NetworkInterfaceProperties
    from .schedule_creation_parameter import ScheduleCreationParameter
    from .lab_virtual_machine_creation_parameter import LabVirtualMachineCreationParameter
    from .formula_properties_from_vm import FormulaPropertiesFromVm
    from .formula import Formula
    from .gallery_image_reference_fragment import GalleryImageReferenceFragment
    from .inbound_nat_rule_fragment import InboundNatRuleFragment
    from .shared_public_ip_address_configuration_fragment import SharedPublicIpAddressConfigurationFragment
    from .network_interface_properties_fragment import NetworkInterfacePropertiesFragment
    from .schedule_creation_parameter_fragment import ScheduleCreationParameterFragment
    from .lab_virtual_machine_creation_parameter_fragment import LabVirtualMachineCreationParameterFragment
    from .formula_properties_from_vm_fragment import FormulaPropertiesFromVmFragment
    from .formula_fragment import FormulaFragment
    from .gallery_image import GalleryImage
    from .parameter_info import ParameterInfo
    from .generate_arm_template_request import GenerateArmTemplateRequest
    from .generate_upload_uri_parameter import GenerateUploadUriParameter
    from .generate_upload_uri_response import GenerateUploadUriResponse
    from .identity_properties import IdentityProperties
    from .import_lab_virtual_machine_request import ImportLabVirtualMachineRequest
    from .lab_announcement_properties import LabAnnouncementProperties
    from .lab_support_properties import LabSupportProperties
    from .lab import Lab
    from .lab_announcement_properties_fragment import LabAnnouncementPropertiesFragment
    from .target_cost_properties import TargetCostProperties
    from .lab_cost_summary_properties import LabCostSummaryProperties
    from .lab_cost_details_properties import LabCostDetailsProperties
    from .lab_resource_cost_properties import LabResourceCostProperties
    from .lab_cost import LabCost
    from .lab_support_properties_fragment import LabSupportPropertiesFragment
    from .lab_fragment import LabFragment
    from .lab_vhd import LabVhd
    from .lab_virtual_machine import LabVirtualMachine
    from .lab_virtual_machine_fragment import LabVirtualMachineFragment
    from .notification_channel import NotificationChannel
    from .notification_channel_fragment import NotificationChannelFragment
    from .notify_parameters import NotifyParameters
    from .operation_error import OperationError
    from .operation_metadata_display import OperationMetadataDisplay
    from .operation_metadata import OperationMetadata
    from .operation_result import OperationResult
    from .policy import Policy
    from .policy_fragment import PolicyFragment
    from .port import Port
    from .port_fragment import PortFragment
    from .rdp_connection import RdpConnection
    from .resize_lab_virtual_machine_properties import ResizeLabVirtualMachineProperties
    from .resource import Resource
    from .retarget_schedule_properties import RetargetScheduleProperties
    from .secret import Secret
    from .secret_fragment import SecretFragment
    from .service_fabric import ServiceFabric
    from .service_fabric_fragment import ServiceFabricFragment
    from .service_runner import ServiceRunner
    from .shutdown_notification_content import ShutdownNotificationContent
    from .subnet import Subnet
    from .subnet_fragment import SubnetFragment
    from .subnet_shared_public_ip_address_configuration import SubnetSharedPublicIpAddressConfiguration
    from .subnet_override import SubnetOverride
    from .subnet_shared_public_ip_address_configuration_fragment import SubnetSharedPublicIpAddressConfigurationFragment
    from .subnet_override_fragment import SubnetOverrideFragment
    from .update_resource import UpdateResource
    from .user_identity import UserIdentity
    from .user_secret_store import UserSecretStore
    from .user import User
    from .user_identity_fragment import UserIdentityFragment
    from .user_secret_store_fragment import UserSecretStoreFragment
    from .user_fragment import UserFragment
    from .virtual_network import VirtualNetwork
    from .virtual_network_fragment import VirtualNetworkFragment
from .operation_metadata_paged import OperationMetadataPaged
from .lab_paged import LabPaged
from .lab_vhd_paged import LabVhdPaged
from .schedule_paged import SchedulePaged
from .artifact_source_paged import ArtifactSourcePaged
from .arm_template_paged import ArmTemplatePaged
from .artifact_paged import ArtifactPaged
from .custom_image_paged import CustomImagePaged
from .formula_paged import FormulaPaged
from .gallery_image_paged import GalleryImagePaged
from .notification_channel_paged import NotificationChannelPaged
from .policy_paged import PolicyPaged
from .service_runner_paged import ServiceRunnerPaged
from .user_paged import UserPaged
from .disk_paged import DiskPaged
from .dtl_environment_paged import DtlEnvironmentPaged
from .secret_paged import SecretPaged
from .service_fabric_paged import ServiceFabricPaged
from .lab_virtual_machine_paged import LabVirtualMachinePaged
from .virtual_network_paged import VirtualNetworkPaged
from .dev_test_labs_client_enums import (
    EnableStatus,
    SourceControlType,
    StorageType,
    CostThresholdStatus,
    WindowsOsState,
    LinuxOsState,
    CustomImageOsType,
    HostCachingOptions,
    NotificationChannelEventType,
    TransportProtocol,
    VirtualMachineCreationSource,
    FileUploadOptions,
    PremiumDataDisk,
    EnvironmentPermission,
    TargetCostStatus,
    ReportingCycleType,
    CostType,
    HttpStatusCode,
    PolicyStatus,
    PolicyFactName,
    PolicyEvaluatorType,
    UsagePermissionType,
)

__all__ = [
    'WeekDetails',
    'DayDetails',
    'HourDetails',
    'NotificationSettings',
    'Schedule',
    'ApplicableSchedule',
    'WeekDetailsFragment',
    'DayDetailsFragment',
    'HourDetailsFragment',
    'NotificationSettingsFragment',
    'ScheduleFragment',
    'ApplicableScheduleFragment',
    'ArtifactParameterProperties',
    'ArtifactInstallProperties',
    'ApplyArtifactsRequest',
    'ParametersValueFileInfo',
    'ArmTemplate',
    'ArmTemplateInfo',
    'ArmTemplateParameterProperties',
    'ArmTemplateParameterPropertiesFragment',
    'Artifact',
    'ArtifactDeploymentStatusProperties',
    'ArtifactDeploymentStatusPropertiesFragment',
    'ArtifactParameterPropertiesFragment',
    'ArtifactInstallPropertiesFragment',
    'ArtifactSource',
    'ArtifactSourceFragment',
    'AttachDiskProperties',
    'AttachNewDataDiskOptions',
    'AttachNewDataDiskOptionsFragment',
    'BulkCreationParameters',
    'BulkCreationParametersFragment',
    'ComputeDataDisk',
    'ComputeDataDiskFragment',
    'ComputeVmInstanceViewStatus',
    'ComputeVmInstanceViewStatusFragment',
    'ComputeVmProperties',
    'ComputeVmPropertiesFragment',
    'PercentageCostThresholdProperties',
    'CostThresholdProperties',
    'WindowsOsInfo',
    'LinuxOsInfo',
    'CustomImagePropertiesFromVm',
    'CustomImagePropertiesCustom',
    'DataDiskStorageTypeInfo',
    'CustomImagePropertiesFromPlan',
    'CustomImage',
    'WindowsOsInfoFragment',
    'LinuxOsInfoFragment',
    'CustomImagePropertiesFromVmFragment',
    'CustomImagePropertiesCustomFragment',
    'DataDiskStorageTypeInfoFragment',
    'CustomImagePropertiesFromPlanFragment',
    'CustomImageFragment',
    'DataDiskProperties',
    'DataDiskPropertiesFragment',
    'DetachDataDiskProperties',
    'DetachDiskProperties',
    'Disk',
    'DiskFragment',
    'EnvironmentDeploymentProperties',
    'DtlEnvironment',
    'EnvironmentDeploymentPropertiesFragment',
    'DtlEnvironmentFragment',
    'EvaluatePoliciesProperties',
    'EvaluatePoliciesRequest',
    'PolicyViolation',
    'PolicySetResult',
    'EvaluatePoliciesResponse',
    'Event',
    'EventFragment',
    'ExportResourceUsageParameters',
    'ExternalSubnet',
    'ExternalSubnetFragment',
    'GalleryImageReference',
    'InboundNatRule',
    'SharedPublicIpAddressConfiguration',
    'NetworkInterfaceProperties',
    'ScheduleCreationParameter',
    'LabVirtualMachineCreationParameter',
    'FormulaPropertiesFromVm',
    'Formula',
    'GalleryImageReferenceFragment',
    'InboundNatRuleFragment',
    'SharedPublicIpAddressConfigurationFragment',
    'NetworkInterfacePropertiesFragment',
    'ScheduleCreationParameterFragment',
    'LabVirtualMachineCreationParameterFragment',
    'FormulaPropertiesFromVmFragment',
    'FormulaFragment',
    'GalleryImage',
    'ParameterInfo',
    'GenerateArmTemplateRequest',
    'GenerateUploadUriParameter',
    'GenerateUploadUriResponse',
    'IdentityProperties',
    'ImportLabVirtualMachineRequest',
    'LabAnnouncementProperties',
    'LabSupportProperties',
    'Lab',
    'LabAnnouncementPropertiesFragment',
    'TargetCostProperties',
    'LabCostSummaryProperties',
    'LabCostDetailsProperties',
    'LabResourceCostProperties',
    'LabCost',
    'LabSupportPropertiesFragment',
    'LabFragment',
    'LabVhd',
    'LabVirtualMachine',
    'LabVirtualMachineFragment',
    'NotificationChannel',
    'NotificationChannelFragment',
    'NotifyParameters',
    'OperationError',
    'OperationMetadataDisplay',
    'OperationMetadata',
    'OperationResult',
    'Policy',
    'PolicyFragment',
    'Port',
    'PortFragment',
    'RdpConnection',
    'ResizeLabVirtualMachineProperties',
    'Resource',
    'RetargetScheduleProperties',
    'Secret',
    'SecretFragment',
    'ServiceFabric',
    'ServiceFabricFragment',
    'ServiceRunner',
    'ShutdownNotificationContent',
    'Subnet',
    'SubnetFragment',
    'SubnetSharedPublicIpAddressConfiguration',
    'SubnetOverride',
    'SubnetSharedPublicIpAddressConfigurationFragment',
    'SubnetOverrideFragment',
    'UpdateResource',
    'UserIdentity',
    'UserSecretStore',
    'User',
    'UserIdentityFragment',
    'UserSecretStoreFragment',
    'UserFragment',
    'VirtualNetwork',
    'VirtualNetworkFragment',
    'OperationMetadataPaged',
    'LabPaged',
    'LabVhdPaged',
    'SchedulePaged',
    'ArtifactSourcePaged',
    'ArmTemplatePaged',
    'ArtifactPaged',
    'CustomImagePaged',
    'FormulaPaged',
    'GalleryImagePaged',
    'NotificationChannelPaged',
    'PolicyPaged',
    'ServiceRunnerPaged',
    'UserPaged',
    'DiskPaged',
    'DtlEnvironmentPaged',
    'SecretPaged',
    'ServiceFabricPaged',
    'LabVirtualMachinePaged',
    'VirtualNetworkPaged',
    'EnableStatus',
    'SourceControlType',
    'StorageType',
    'CostThresholdStatus',
    'WindowsOsState',
    'LinuxOsState',
    'CustomImageOsType',
    'HostCachingOptions',
    'NotificationChannelEventType',
    'TransportProtocol',
    'VirtualMachineCreationSource',
    'FileUploadOptions',
    'PremiumDataDisk',
    'EnvironmentPermission',
    'TargetCostStatus',
    'ReportingCycleType',
    'CostType',
    'HttpStatusCode',
    'PolicyStatus',
    'PolicyFactName',
    'PolicyEvaluatorType',
    'UsagePermissionType',
]
