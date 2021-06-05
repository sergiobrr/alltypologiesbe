from django.db import IntegrityError
from model_mommy import mommy
from ..models import Project, Offer
from django.test import TestCase


class TestProject(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.project = mommy.make('annotator.Project')

    def test_str_contains_class_name(self):
        self.assertTrue(
            self.project.__str__().startswith('Project')
        )

    def test_get_absolute_url(self):
        expected_url = f'/api/v1/projects/{self.project.id}/'
        self.assertEqual(expected_url, self.project.get_absolute_url())

    def test_project_name_uniqueness(self):
        duplicated_project = Project(
            name=self.project.name, description='Description', randomize_document_order=False
        )
        self.assertRaises(
            IntegrityError, duplicated_project.save
        )


class TestOffer(TestCase):
    offers = [
'10097 Natura Oil con Olio di Cocco Bio Balsamo 100 ml Natura Oil è una nuova linea a base di oli certificati BIO, ricchi di vitamine (A, C, B3, E), di minerali (Potassio, Fosforo, Sodio, Calcio, Magnesio e Ferro), di Acidi grassi, sostanze fondamentali per il nostro benessere. I prodotti Natura Oil sono un',
'10097 Natura Oil Olio di Argan Doccia 100 ml Natura Oil è una nuova linea a base di oli certificati BIO, ricchi di vitamine (A, C, B3, E), di minerali (Potassio, Fosforo, Sodio, Calcio, Magnesio e Ferro), di Acidi grassi, sostanze fondamentali per il nostro benessere. I prodotti Natura Oil sono un',
'10097 Natura Oil Olio di Argan Doccia 100 ml Natura Oil è una nuova linea a base di oli certificati BIO, ricchi di vitamine (A, C, B3, E), di minerali (Potassio, Fosforo, Sodio, Calcio, Magnesio e Ferro), di Acidi grassi, sostanze fondamentali per il nostro benessere. I prodotti Natura Oil sono un',
'100Bon Eau De Parfum - 50 Ml 100Bon Eau De Parfum - 50 Ml Fragranze e profumi: eau de parfum Contentuo: 50 millilitri Eau de parfum unisex 50 millilitri',
'100Bon Eau De Parfum - 50 Ml 100Bon Eau De Parfum - 50 Ml Fragranze e profumi: eau de parfum Contentuo: 50 millilitri Eau de parfum unisex 50 millilitri',
]

    @classmethod
    def setUpTestData(cls):
        cls.project = mommy.make('annotator.Project')
        for t in cls.offers:
            mommy.make('annotator.Offer', text=t, project=cls.project)

    def test_full_text_search(self):
        from django.contrib.postgres.search import SearchQuery
        from annotator.models import offers_search_vector as s
        query = SearchQuery("'doccia' OR 'profumi'", config='italian', search_type='websearch')
        results = Offer.objects.annotate(search=s).filter(search=query).values_list('text', flat=True)
        # not matching
        self.assertNotIn(self.offers[0], results)
        for i in range(1, 4):
            # matching
            self.assertIn(self.offers[i], results)
