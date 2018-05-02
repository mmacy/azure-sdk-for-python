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

from msrest.serialization import Model


class QueryExecutionResult(Model):
    """Describes query analysis results for execution in source and target.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar query_text: Query text retrieved from the source server
    :vartype query_text: str
    :ivar statements_in_batch: Total no. of statements in the batch
    :vartype statements_in_batch: long
    :ivar source_result: Query analysis result from the source
    :vartype source_result:
     ~azure.mgmt.datamigration.models.ExecutionStatistics
    :ivar target_result: Query analysis result from the target
    :vartype target_result:
     ~azure.mgmt.datamigration.models.ExecutionStatistics
    """

    _validation = {
        'query_text': {'readonly': True},
        'statements_in_batch': {'readonly': True},
        'source_result': {'readonly': True},
        'target_result': {'readonly': True},
    }

    _attribute_map = {
        'query_text': {'key': 'queryText', 'type': 'str'},
        'statements_in_batch': {'key': 'statementsInBatch', 'type': 'long'},
        'source_result': {'key': 'sourceResult', 'type': 'ExecutionStatistics'},
        'target_result': {'key': 'targetResult', 'type': 'ExecutionStatistics'},
    }

    def __init__(self, **kwargs) -> None:
        super(QueryExecutionResult, self).__init__(**kwargs)
        self.query_text = None
        self.statements_in_batch = None
        self.source_result = None
        self.target_result = None
