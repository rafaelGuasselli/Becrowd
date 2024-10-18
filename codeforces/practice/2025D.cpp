#include<bits/stdc++.h>
//#define int long long
using namespace std;

int dp[5001][5001];
int valores[2000005];
int smartRange[5001][5001];
int strengthRange[5001][5001];
	
signed main() {
	int n, m; cin>>n>>m;
	for (int i = 0; i < n; i++) {
		cin>>valores[i];
	}

	int zeroIndex = 0;
	for (int i = 0; i < n; i++) {
		if (valores[i] == 0) {
			zeroIndex++;
			continue;
		}

		if (valores[i] > 0) {
			smartRange[zeroIndex][valores[i]]++;
		} else {
			strengthRange[zeroIndex][-valores[i]]++;
		}
	}

	
	for (int xp = 1; xp <= m; xp++) {
		int acumulated = 0;
		for (int i = xp; i >= 0; i--) {
			acumulated += strengthRange[xp][i];
		}

		for (int smart = 0; smart <= xp; smart++) {
			int strength = xp - smart;
			acumulated += smartRange[xp][smart];
			if(strength-1 > 0) {
				acumulated -= strengthRange[xp][strength-1];
			}

			dp[xp][smart] = max(dp[xp-1][smart-1], dp[xp-1][smart]) + acumulated; 
		}
	}

	int maximo = 0;
	for (int i = 0; i <= m; i++) {
		maximo = max(maximo, dp[m][i]);
	}
	
	cout<<maximo<<endl;
	return 0;
}