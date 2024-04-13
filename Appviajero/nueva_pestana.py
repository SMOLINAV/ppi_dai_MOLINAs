def abrir_nueva_pestana():
    return """
        <script>
        var newTab = window.open("", "_blank");
        newTab.document.write('<h1 style="text-align:center">Busca tu próximo destino</h1>');
        newTab.document.write('<form action="https://www.google.com/search" method="get" target="_blank" style="text-align:center">');
        newTab.document.write('<input type="text" name="q" placeholder="Buscar en Google" style="width: 50%; padding: 10px; margin: 10px 0;">');
        newTab.document.write('<input type="submit" value="Buscar" style="padding: 10px; margin: 10px 0; cursor: pointer;">');
        newTab.document.write('</form>');
        </script>
        """
