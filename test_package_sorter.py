import unittest
from package_sorter import sort, is_bulky, is_heavy


class TestPackageSorter(unittest.TestCase):
    
    def test_is_bulky_by_volume(self):
        """Test bulky detection based on volume >= 1,000,000 cm³."""
        self.assertTrue(is_bulky(100, 100, 100))  # 1,000,000 cm³
        
        # Just above threshold
        self.assertTrue(is_bulky(100, 100, 101))  # 1,010,000 cm³
        
        # Just below threshold
        self.assertFalse(is_bulky(99, 99, 99))    # 970,299 cm³
    
    def test_is_bulky_by_dimension(self):
        """Test bulky detection based on any dimension >= 150 cm."""
        # Exactly at threshold
        self.assertTrue(is_bulky(150, 10, 10))    # width = 150
        self.assertTrue(is_bulky(10, 150, 10))    # height = 150
        self.assertTrue(is_bulky(10, 10, 150))    # length = 150
        
        # Just above threshold
        self.assertTrue(is_bulky(151, 10, 10))    # width = 151
        
        # Just below threshold
        self.assertFalse(is_bulky(149, 10, 10))   # width = 149
        self.assertFalse(is_bulky(10, 149, 10))   # height = 149
        self.assertFalse(is_bulky(10, 10, 149))   # length = 149
    
    def test_is_heavy(self):
        """Test heavy detection based on mass >= 20 kg."""
        # Exactly at threshold
        self.assertTrue(is_heavy(20))
        
        # Just above threshold
        self.assertTrue(is_heavy(20.1))
        
        # Just below threshold
        self.assertFalse(is_heavy(19.9))
        
        # Much lighter
        self.assertFalse(is_heavy(5))
    
    def test_standard_packages(self):
        """Test packages that should go to STANDARD stack."""
        # Small and light
        self.assertEqual(sort(10, 10, 10, 5), "STANDARD")
          
    def test_special_packages_bulky_only(self):
        """Test packages that are bulky but not heavy -> SPECIAL."""
        # Bulky by volume, light weight
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")
        
        # Bulky by dimension, light weight
        self.assertEqual(sort(10, 200, 10, 15), "SPECIAL")
    
    def test_special_packages_heavy_only(self):
        """Test packages that are heavy but not bulky -> SPECIAL."""
        # Heavy but small volume and dimensions
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")
    
    def test_rejected_packages(self):
        """Test packages that are both bulky and heavy -> REJECTED."""
        # Bulky by volume and heavy
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")
        
        # Bulky by dimension and heavy
        self.assertEqual(sort(10, 200, 10, 30), "REJECTED")
        
        # Very large and very heavy
        self.assertEqual(sort(200, 200, 200, 100), "REJECTED")

    



if __name__ == "__main__":
    unittest.main(verbosity=2)
