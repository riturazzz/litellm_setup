# Use LiteLLM as proxy

## Try various models without changing your Chat interface
- Create a folder named `litellm`
- Clone this repo content inside it
- Create a key for LiteLLM proxy server using command : `echo "sk-$(openssl rand -base64 32)"`
- Copy the `.env.example` file to `.env` and update the variable values
- Add db connection string as well as redis connection details in `litellm_config.yaml` **general_settings**
- Add your required LLM provider and model details in `litellm_config.yaml`
- Run : `docker compose up -d`
