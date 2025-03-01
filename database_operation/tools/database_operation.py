from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class DatabaseOperationTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        sql = tool_parameters.get('sql')
        output_format = tool_parameters.get('output_format', 'json')
        dbsystem = tool_parameters.get('dbsystem')
        host = tool_parameters.get('host')
        port = tool_parameters.get('port')
        username = tool_parameters.get('username')
        password = tool_parameters.get('password')
        dbname = tool_parameters.get('dbname')

        

        message = "Hello, World!"
        yield self.create_text_message(message)