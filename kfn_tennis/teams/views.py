from django.shortcuts import render, get_object_or_404
from .models import Player, Season

def teams_view(request):
    seasons = Season.objects.all().order_by('-year')
    
    season_id = request.GET.get('season')
    search_query = request.GET.get('q', '').strip()

    if season_id:
        season = get_object_or_404(Season, id=season_id)
        players = season.players.all()
        team_pdf = season.team_list_pdf.url if season.team_list_pdf else None
    else:
        season = None
        players = Player.objects.all()
        team_pdf = None

    if search_query:
        players = players.filter(full_name__icontains=search_query)

    context = {
        'seasons': seasons,
        'players': players,
        'selected_season': season_id,
        'team_pdf': team_pdf,
        'search_query': search_query,
    }
    return render(request, 'teams/teams.html', context)
