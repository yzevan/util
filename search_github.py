import github
import sys

def get_max_width(table, index):
    """Get the maximum width of the given column index"""
    return max([len(unicode(row[index])) for row in table])

def pprint_table(out, table):
    """Prints out a table of data, padded for alignment
    @param out: Output stream (file-like object)
    @param table: The table to print. A list of lists.
    Each row must have the same number of columns. """
    col_paddings = []

    for i in range(len(table[0])):
        col_paddings.append(get_max_width(table, i))

    for row in table:
        # left col
        print >> out, row[0].ljust(col_paddings[0] + 1),
        # middle cols
        for i in range(1, len(row)-1):
            col = unicode(row[i]).rjust(col_paddings[i] + 2)
            print >> out, col,
	#last col
	print >> out, row[len(row)-1]
        #print >> out
	

hub = github.Github()
keyword = "daily show"
language = "python"
limit = 200
repo_list = hub.legacy_search_repos(keyword, language)

final_repo_list = []

i = 1
for repo in repo_list:
	#print i, repo.name.rjust(20),  str(repo.forks).rjust(5), str(repo.watchers).rjust(5), unicode(repo.description), repo.created_at, repo.pushed_at
	final_repo_list.append( (repo.name, repo.forks, repo.watchers, repo.pushed_at, repo.description))
	i = i+1
	if i > limit:
		break

#In cmp function, we compare "watchers" field of each repo
final_repo_list.sort(cmp = lambda x,y: cmp(x[2], y[2]) , key=None, reverse=True)
pprint_table(sys.stdout, final_repo_list)

