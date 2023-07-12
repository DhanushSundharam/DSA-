class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    def add_child(self, child):
        child.parent = self
        self.children.append(child)    

    def print_tree(self):
        if self.data == "Vinaichsol":  # Check if node is "verbs"
            for child in self.children:
                print(child.data)
        else:
            print(self.data)
            if self.children:
                for child in self.children:
                    child.print_tree()

def bulid_product_tree():
    root=TreeNode("Pechin paguthi")

    verbs=TreeNode("Vinaichsol")
    verbs.add_child(TreeNode("seyal viṉaigaḷ"))
    verbs.add_child(TreeNode("Nilaiyāṉa viṉaichsoṟgaḷ"))
    verbs.add_child(TreeNode("Idainilai viṉaichsoṟgaḷ"))
    verbs.add_child(TreeNode("māṟāta viṉaiccoṟkaḷ"))
    verbs.add_child(TreeNode("viṉaiccoṟkaḷai iṇaittal"))
    verbs.add_child(TreeNode("utavum viṉaiccoṟkaḷ"))
    verbs.add_child(TreeNode("mātiri viṉaiccoṟkaḷ"))
    verbs.add_child(TreeNode("vaḻakkamāṉa viṉaiccol"))
    verbs.add_child(TreeNode("oḻuṅkaṟṟa viṉaiccoṟkaḷ"))
    verbs.add_child(TreeNode("coṟṟoṭar viṉaiccoṟkaḷ"))
    verbs.add_child(TreeNode("muṭivili viṉaiccoṟkaḷ"))

    Adverb=TreeNode("Viṉaiyuriccoṟkaḷ")
    Adverb.add_child(TreeNode("Vitattai vivarikkum viṉaiyuriccoṟkaḷ"))
    Adverb.add_child(TreeNode("iṭattiṉ viṉaiyuriccoṟkaḷ"))
    Adverb.add_child(TreeNode("kālattiṉ viṉaiyuriccoṟkaḷ"))
    Adverb.add_child(TreeNode("atirveṇṇiṉ viṉaiyuriccoṟkaḷ"))
    Adverb.add_child(TreeNode("paṭṭattiṉ viṉaiyuriccoṟkaḷ"))

    Noun=TreeNode("Peyarccoṟkaḷ")
    Noun.add_child(TreeNode("seriyāṉa peyarccoṟkaḷ"))
    Noun.add_child(TreeNode("potuvāṉa peyarccoṟkaḷ"))
    Noun.add_child(TreeNode("orumai peyarccoṟkaḷ"))
    Noun.add_child(TreeNode("paṉmai peyarccol"))
    Noun.add_child(TreeNode("eṇṇakkūṭiya peyarccoṟkaḷ"))
    Noun.add_child(TreeNode("kaṇakkiṭa muṭiyāta peyarccoṟkaḷ"))
    Noun.add_child(TreeNode("kūṭṭu peyarccoṟkaḷ"))
    Noun.add_child(TreeNode("kāṉkirīṭ peyarccoṟkaḷ"))
    Noun.add_child(TreeNode("curukka peyarccoṟkaḷ"))

    pronoun=TreeNode("Piratipeyarkaḷai")
    pronoun.add_child(TreeNode("Uṟaviṉar piratipeyarkaḷ"))
    pronoun.add_child(TreeNode("uṭaimai piratipeyarkaḷ"))
    pronoun.add_child(TreeNode("pirati peyarccoṟkaḷ"))
    pronoun.add_child(TreeNode("ārppāṭṭa piratipeyarkaḷ"))
    pronoun.add_child(TreeNode("kēḷvikkuriya piratipeyarkaḷ"))
    pronoun.add_child(TreeNode("kālavaraiyaṟṟa piratipeyarkaḷai"))
    pronoun.add_child(TreeNode("taṉippaṭṭa piratipeyarkaḷai"))
    pronoun.add_child(TreeNode("poruḷ piratipeyarkaḷ"))
    pronoun.add_child(TreeNode("poruḷ piratipeyarkaḷ"))
    pronoun.add_child(TreeNode("paraspara piratipeyarkaḷ"))
    pronoun.add_child(TreeNode("tīvira piratipeyarkaḷ"))

    Adjective=TreeNode("Urichsol")
    Adjective.add_child(TreeNode("Uṭaimai uriccoṟkaḷ"))
    Adjective.add_child(TreeNode("kēḷvikkuriya uriccoṟkaḷ"))
    Adjective.add_child(TreeNode("ārppāṭṭa uriccoṟkaḷ"))
    Adjective.add_child(TreeNode("kūṭṭu uriccoṟkaḷ"))

    Preposition=TreeNode("Munmolivu")
    Preposition.add_child(TreeNode("Nērattiṉ muṉmoḻivukaḷ"))
    Preposition.add_child(TreeNode("iṭattiṉ muṉmoḻivukaḷ"))
    Preposition.add_child(TreeNode("ticaiyiṉ muṉmoḻivukaḷ"))
    Preposition.add_child(TreeNode("iruppiṭattiṉ muṉmoḻivukaḷ"))
    Preposition.add_child(TreeNode("muṉṉiṭai coṟṟoṭar"))

    Conjunction=TreeNode("Iṇaippusorgal")
    Conjunction.add_child(TreeNode("Oruṅkiṇaippu iṇaippukaḷ"))
    Conjunction.add_child(TreeNode("tuṇai iṇaippukaḷ"))
    Conjunction.add_child(TreeNode("toṭarpu iṇaippukaḷ"))
    Conjunction.add_child(TreeNode("iṇainta viṉaiyuriccoṟkaḷ"))


    interjection=TreeNode("Idaichsol")
    interjection.add_child(TreeNode("Mutaṉmai iṭaiccol"))
    interjection.add_child(TreeNode("iraṇṭām nilai iṭaiccol"))
    interjection.add_child(TreeNode("lēcāṉa iṭaiccol"))
    interjection.add_child(TreeNode("valuvāṉa iṭaiccol"))
    interjection.add_child(TreeNode("vōliṭiv iṭaiccerukal"))
    interjection.add_child(TreeNode("uṇarcci iṭaiccerukal"))
    interjection.add_child(TreeNode("aṟivāṟṟal iṭaiccerukal"))

    root.add_child(verbs)
    root.add_child(Adverb)
    root.add_child(Noun)
    root.add_child(pronoun)
    root.add_child(Adjective)
    root.add_child(Preposition)
    root.add_child(Conjunction)
    root.add_child(interjection)

    return root
    
root=bulid_product_tree()
root.print_tree()