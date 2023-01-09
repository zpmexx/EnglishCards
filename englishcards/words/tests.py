from django.test import TestCase
from .models import MemoryCard
# Create your tests here.


class TestUserModel(TestCase):
    
    def test_if_card_inserted(self):
        self.card1 = MemoryCard.objects.create(
            polishName = 'kot',
            englishName = 'cat',
            polishDescription = 'zwierzę domowe',
            englishDescription = 'house animal',
        )
        
        self.assertIsNotNone(self.card1)
    
    def test_card_with_wrong_wordlevel(self):
        self.card1 = MemoryCard.objects.create(
            polishName = 'kot',
            englishName = 'cat',
            polishDescription = 'zwierzę domowe',
            englishDescription = 'house animal',
            wordLevel = 'wronglevel'
        )
        
        self.assertIsNotNone(self.card1)
