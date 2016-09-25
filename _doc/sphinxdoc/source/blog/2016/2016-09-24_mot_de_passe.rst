

.. blogpost::
    :title: Eviter les mots de passe dans les notebooks
    :keywords: password, mot de passe, notebook, keyring
    :date: 2016-09-24
    :categories: cours
    
    Il arrive fréquemment qu'on ait besoin d'une ressource
    protégée par un mot de passe, service web, API, login
    et le plus simple est toujours d'écire ce mot de passe en
    clair dans le notebook. On se dit qu'il faudra penser à l'enlever 
    avant de partager le notebook et on oublie toujours de l'enlever.
    C'est mon cas en tout cas. J'ai dû plusieurs fois changer de mot 
    de passe car le précédent est parti sur GitHub par inadvertance
    (programmée).
    
    Ma première réponse à ce mécanisme était d'ouvrir un formulaire 
    javascript dans le notebook. J'ai créé la fonction
    `open_html_form <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/pyquickhelper/ipythonhelper/html_forms.html?highlight=html%20form#module-pyquickhelper.ipythonhelper.html_forms>`_.
    Cette solution est pratique mais elle implique de rentrer le mot
    de passe à chaque fois qu'on ouvre le notebook.
    Et elle ne sert à rien pour les notebooks.
    
    La seconde réponse et à mon avis la meilleur est d'utiliser le 
    module `keyring <http://pythonhosted.org/keyring/>`_. D'un côté,
    on écrit ceci sur une ligne de commande Python une et une seule fois :
    
    ::
    
        import keyring
        keyring.set_password("actuariat", "dupre", "mon mot de passe")
        
    Puis dans le notebook, il suffit d'exécuter le code suivant pour récupérer 
    le mot de passe :
    
    ::
    
        import keyring
        keyring.get_password("actuariat", "dupre")
    
    Le mot de passe n'apparaît pas dans le notebook, il n'est pas besoin 
    de le saisir à chaque fois qu'on se sert du notebook et il peut tout aussi
    bien servier pour récupérer le notebook dans un test unitaire.
