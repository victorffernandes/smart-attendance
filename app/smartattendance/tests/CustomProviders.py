from faker.providers import DynamicProvider

semestre_provider = DynamicProvider(
     provider_name="semestre",
     elements=["2023.1", "2023.2", "2022.1", "2024.1", "2022.2"],
)

turma_provider = DynamicProvider(
     provider_name="turma_nome",
     elements=["ES2", "BD1", "BD2", "ED", "ES1"],
)