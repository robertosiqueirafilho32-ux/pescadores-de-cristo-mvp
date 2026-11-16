
from django.test import TestCase
from .models import Beneficiario


class BeneficiarioModelTest(TestCase):

    def setUp(self):
        self.beneficiario = Beneficiario.objects.create(
            nome="João da Silva",
            telefone="11999999999",
            comunidade="Comunidade Central"
        )

    def test_criar_beneficiario(self):
        self.assertEqual(self.beneficiario.nome, "João da Silva")
        self.assertEqual(self.beneficiario.telefone, "11999999999")
        self.assertEqual(
            self.beneficiario.comunidade,
            "Comunidade Central"
        )

    def test_beneficiario_ativo_por_padrao(self):
        self.assertTrue(self.beneficiario.ativo)

    def test_data_cadastro_automatica(self):
        self.assertIsNotNone(self.beneficiario.data_cadastro)

    def test_representacao_em_texto(self):
        self.assertEqual(str(self.beneficiario), "João da Silva")

    def test_consultar_beneficiario_no_banco(self):
        beneficiario = Beneficiario.objects.get(
            id=self.beneficiario.id
        )
        self.assertEqual(beneficiario.nome, "João da Silva")

