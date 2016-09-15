from django.test import TestCase
from item.models import Category, CategoryImage, Script, ScriptParam
from django_comments.models import Comment
import tempfile
# Create your tests here.
class TestCategory(TestCase):
    def setUp(self):
        top = Category.objects.create(name='top',short_desc='short')
        image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        top_leaf = Category.objects.create(name='top_leaf',short_desc='short', full_desc='full', image=image)
        middle = Category.objects.create(name='middle',short_desc='short', parent = top)
        leaf = Category.objects.create(name='leaf',short_desc='short', parent = middle)
        leaf_one = Category.objects.create(name='leaf_one',short_desc='short', parent = middle)
        leaf_empty = Category.objects.create(name='leaf_empty', short_desc='short', parent=middle)

        sc_s = Script.objects.create(name='Sc_s', short_desc='short', category=leaf)
        sc_f = Script.objects.create(name='Sc_f', short_desc='short', full_desc='full', category=leaf_one)

    def test_get_items(self):
        top = Category.objects.get(name='top')
        middle = Category.objects.get(name='middle')
        leaf = Category.objects.get(name='leaf')
        leaf_one = Category.objects.get(name='leaf_one')
        leaf_empty = Category.objects.get(name='leaf_empty')
        m_items = middle.get_items()
        l_items = leaf.get_items()
        lo_items = leaf_one.get_items()
        t_items = top.get_items()
        e_items = leaf_empty.get_items()
        self.assertEqual(len(m_items),2)
        self.assertEqual(len(l_items),1)
        self.assertEqual(len(lo_items),1)
        self.assertEqual(len(t_items), 2)
        self.assertEqual(len(e_items), 0)
        self.assertEqual(m_items[0].name,'Sc_s')
        self.assertEqual(m_items[1].name, 'Sc_f')

    def test_get_url(self):
        top = Category.objects.get(name='top')
        top_pk = 1
        url = top.get_url()
        self.assertEqual(url,'/ru/items/category/1')


    def test_str(self):
        top = Category.objects.get(name = 'top')
        self.assertEqual(str(top),'top')

    def test_get_top_list(self):
        top_list = Category.get_top_list()
        top = Category.objects.get(name='top')
        top_leaf = Category.objects.get(name='top_leaf')
        middle = Category.objects.get(name='middle')
        leaf = Category.objects.get(name='leaf')
        self.assertEqual(top in top_list,True)
        self.assertEqual(top_leaf in top_list, True)
        self.assertEqual(middle in top_list, False)
        self.assertEqual(leaf in top_list, False)

    def test_has_image(self):
        top = Category.objects.get(name='top')
        top_leaf = Category.objects.get(name='top_leaf')
        self.assertEqual(False,top.has_image())
        self.assertEqual(True,top_leaf.has_image())

    def test_get_full_desc(self):
        top = Category.objects.get(name='top')
        top_leaf = Category.objects.get(name='top_leaf')
        self.assertEqual(top.get_full_desc(),'short')
        self.assertEqual(top_leaf.get_full_desc(), 'full')

    def test_has_parent(self):
        top = Category.objects.get(name='top')
        middle = Category.objects.get(name='middle')
        leaf = Category.objects.get(name='leaf')
        self.assertEqual(False, top.has_parent())
        self.assertEqual(True, middle.has_parent())
        self.assertEqual(True, leaf.has_parent())

    def test_is_top(self):
        top = Category.objects.get(name='top')
        top_leaf = Category.objects.get(name='top_leaf')
        middle = Category.objects.get(name='middle')
        leaf = Category.objects.get(name='leaf')
        self.assertEqual(True, top.is_top())
        self.assertEqual(True, top_leaf.is_top())
        self.assertEqual(False, middle.is_top())
        self.assertEqual(False, leaf.is_top())

    def test_is_leaf(self):
        top = Category.objects.get(name='top')
        middle = Category.objects.get(name='middle')
        leaf = Category.objects.get(name='leaf')
        top_leaf = Category.objects.get(name='top_leaf')
        self.assertEqual(False, top.is_leaf())
        self.assertEqual(False, middle.is_leaf())
        self.assertEqual(True, leaf.is_leaf())
        self.assertEqual(True, top_leaf.is_leaf())

    def test_get_children(self):
        top = Category.objects.get(name='top')
        middle = Category.objects.get(name='middle')
        leaf = Category.objects.get(name='leaf')
        #leaf_one = Category.objects.get(name='leaf_one')
        top_children = top.get_children()
        middle_children = middle.get_children()
        leaf_children = leaf.get_children()
        self.assertEqual('middle',top_children[0].name)
        self.assertEqual('leaf',middle_children[0].name)
        self.assertEqual('leaf_one', middle_children[1].name)
        self.assertEqual(0,len(leaf_children))

    def test_is_middle(self):
        top = Category.objects.get(name='top')
        middle = Category.objects.get(name='middle')
        leaf = Category.objects.get(name='leaf')
        top_leaf = Category.objects.get(name='top_leaf')
        self.assertEqual(False, top.is_middle())
        self.assertEqual(True, middle.is_middle())
        self.assertEqual(False, leaf.is_middle())
        self.assertEqual(False, top_leaf.is_middle())

class TestCategoryImage(TestCase):
    def setUp(self):
        top = Category.objects.create(name='top', short_desc='short')
        image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        category_image = CategoryImage.objects.create(category=top,image=image)

    def test_str(self):
        top = Category.objects.get(name='top')
        category_image = CategoryImage.objects.get(category=top)
        self.assertEqual(str(category_image),'top')

class TestScript(TestCase):
    def setUp(self):
        top = Category.objects.create(name='top', short_desc='short')
        sc_s = Script.objects.create(name='Sc_s', short_desc='short', category=top)
        sc_f = Script.objects.create(name='Sc_f', short_desc='short', full_desc='full', category=top)

    def test_get_full_desc(self):
        sc_s = Script.objects.get(name='Sc_s')
        sc_f = Script.objects.get(name='Sc_f')
        self.assertEqual(sc_s.get_full_desc(), 'short')
        self.assertEqual(sc_f.get_full_desc(), 'full')

    def test_str(self):
        sc_s = Script.objects.get(name='Sc_s')
        self.assertEqual('Sc_s',str(sc_s))

    def test_get_url(self):
        sc_s = Script.objects.get(name='Sc_s')
        url = sc_s.get_url()
        self.assertEqual(url, '/ru/items/script/1')

class TestScriptParam(TestCase):
    def setUp(self):
        top = Category.objects.create(name='top', short_desc='short')
        sc_s = Script.objects.create(name='Sc_s', short_desc='short', category=top)
        param = ScriptParam.objects.create(name='par',script=sc_s,desc='desc',default_value='def_val')

    def test_str(self):
        param = ScriptParam.objects.get(name='par')
        self.assertEqual(str(param),'Sc_s: par, default_value: def_val')