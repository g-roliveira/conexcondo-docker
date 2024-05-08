from xml.etree import ElementTree as ET
import re
import os

def xor_crypt(data, key, encrypt=False):
    key_length = len(key)
    result_data = bytearray(len(data))

    for i in range(len(data)):
        result_data[i] = data[i] ^ key[i % key_length]

    return result_data

def load_and_modify_xml(input_file_path, output_file_path, modifications, xor_key):
    # Descriptografar o arquivo .wfre
    with open(input_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_xml = xor_crypt(encrypted_data, xor_key)

    # Carregar o XML descriptografado
    root = ET.fromstring(decrypted_xml)

    # Encontrar o elemento ROW e modificar os valores
    row = root.find('.//ROW')
    if row is not None:
        param_str = row.get('SIS_PARAMETRO')

        # Modificar cada valor conforme necessário
        for key, new_value in modifications.items():
            # Padrão para corresponder à chave e ao valor atual, considerando a quebra de linha
            pattern = rf'(?m)^({key}=).*?$'
            param_str = re.sub(pattern, lambda m: m.group(1) + new_value, param_str)

        # Atualizar o atributo SIS_PARAMETRO com os novos valores, revertendo as substituições de caracteres
        row.set('SIS_PARAMETRO', param_str)

        # Gerar o novo XML como string e criptografá-lo
        modified_xml = ET.tostring(root, encoding='utf-8', method='xml')
        encrypted_modified_xml = xor_crypt(modified_xml, xor_key, encrypt=True)

        # Salvar o arquivo criptografado
        with open(output_file_path, 'wb') as file:
            file.write(encrypted_modified_xml)

        return True
    return False

# Acessar valores das variáveis de ambiente
modifications = {
    "HostName": os.getenv('WEBRUN_HOST_DB'),
    "User_Name": os.getenv('WEBRUN_USER_DB'),
    "Password": os.getenv('WEBRUN_PASS_DB'),
    "DataBase": os.getenv('WEBRUN_DB'),
    "Port": os.getenv('WEBRUN_PORT_DB'),
}

# Configurações do arquivo e chave XOR
input_file_path = '/usr/local/tomcat/settings/systems/Conexcondo.wfre'  # Atualize isso para o caminho do seu arquivo
output_file_path = '/usr/local/tomcat/settings/systems/Conexcondo.wfre'  # Onde salvar o arquivo modificado
xor_key = b'GDFGERTY4YETHDSGEGF'  # Sua chave XOR real como bytes

# Executar a função de modificação
result = load_and_modify_xml(input_file_path, output_file_path, modifications, xor_key)

if result:
    print("Arquivo .wfre modificado com sucesso e salvo em:", output_file_path)
else:
    print("Falha ao modificar o arquivo .wfre.")
