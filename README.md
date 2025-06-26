This is a companion to my dissertation thesis. 
It contains: 
	- Full lists of Siamese color graphs (SCGs) in binary and base-24 representation divided into three parts by the isomorphism classes of graphs contained within.
		- Binary representations, readable by GAP, are in files "Geometric_SCG_bin_num.txt", "Non-geometric_SCG_bin_num.txt" and "Mixed_SCG_bin_num.txt".
		- Base24 representations, readable by GAP, are in files "Geometric_SCG_base24_num.txt", "Non-geometric_SCG_base24_num.txt" and "Mixed_SCG_base24_num.txt".
		- In the case of mixed SCGs, graphs represented by the first two numbers of the 4-tuple binary representations are non-geometric while graphs represent by the latter two are geometric.
	- Functions to compute adjacency matrices and permutation voltages representations from the number representation and vice versa
		- functions in GAP are in file "transfer_functions_GAP.txt".
	- List of all graphs and tables of interest used during our computations are in file "auxiliary_variables.txt"
	- Trie class (in Python) used during the computations in "trie.py"
