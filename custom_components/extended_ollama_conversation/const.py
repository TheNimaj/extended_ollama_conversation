"""Constants for the Extended Ollama Conversation integration."""

DOMAIN = "extended_ollama_conversation"
DEFAULT_NAME = "Extended Ollama Conversation"
CONF_ORGANIZATION = "organization"
CONF_BASE_URL = "base_url"
DEFAULT_CONF_BASE_URL = "https://api.ollama.com/v1"
CONF_API_VERSION = "api_version"
CONF_SKIP_AUTHENTICATION = "skip_authentication"
DEFAULT_SKIP_AUTHENTICATION = False

EVENT_AUTOMATION_REGISTERED = "automation_registered_via_extended_ollama_conversation"
EVENT_CONVERSATION_FINISHED = "extended_ollama_conversation.conversation.finished"

CONF_PROMPT = "prompt"
DEFAULT_PROMPT = """I want you to act as smart home manager of Home Assistant.
I will provide information of smart home along with a question, you will truthfully make correction or answer using information provided in one sentence in everyday language.

Current Time: {{now()}}

Available Devices:
```csv
entity_id,name,state,aliases
{% for entity in exposed_entities -%}
{{ entity.entity_id }},{{ entity.name }},{{ entity.state }},{{entity.aliases | join('/')}}
{% endfor -%}
```

The current state of devices is provided in available devices.
Use execute_services function to control devices.
You can infer the entity_id from the name and common variations.
Do not as for confirmation to execute a service.
Do not restate or appreciate what user says, rather make a quick inquiry."
"""
CONF_CHAT_MODEL = "chat_model"
DEFAULT_CHAT_MODEL = "llama3.1"
CONF_MAX_TOKENS = "max_tokens"
DEFAULT_MAX_TOKENS = 150
CONF_TOP_P = "top_p"
DEFAULT_TOP_P = 1
CONF_TEMPERATURE = "temperature"
DEFAULT_TEMPERATURE = 0.5
CONF_MAX_FUNCTION_CALLS_PER_CONVERSATION = "max_function_calls_per_conversation"
DEFAULT_MAX_FUNCTION_CALLS_PER_CONVERSATION = 1
CONF_FUNCTIONS = "functions"
DEFAULT_CONF_FUNCTIONS = [
    {
        "spec": {
            "name": "execute_services",
            "description": "Use this function to execute service of devices in Home Assistant.",
            "parameters": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "service": {
                                    "type": "string",
                                    "description": "The service to be called",
                                },
                                 "entity_id": {
                                    "type": "string",
                                    "description": "The entity_id retrieved from available devices. It must start with domain, followed by dot character.",
                                    }
                                },
                            "required": ["entity_id", "service"],
                        },
                    }
                },
            },
        },
        "function": {"type": "native", "name": "execute_service"},
    }
]
CONF_ATTACH_USERNAME = "attach_username"
DEFAULT_ATTACH_USERNAME = False
CONF_USE_TOOLS = "use_tools"
DEFAULT_USE_TOOLS = False
CONF_CONTEXT_THRESHOLD = "context_threshold"
DEFAULT_CONTEXT_THRESHOLD = 13000
CONTEXT_TRUNCATE_STRATEGIES = [{"key": "clear", "label": "Clear All Messages"}]
CONF_CONTEXT_TRUNCATE_STRATEGY = "context_truncate_strategy"
DEFAULT_CONTEXT_TRUNCATE_STRATEGY = CONTEXT_TRUNCATE_STRATEGIES[0]["key"]

SERVICE_QUERY_IMAGE = "query_image"

CONF_PAYLOAD_TEMPLATE = "payload_template"
