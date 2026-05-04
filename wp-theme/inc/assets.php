<?php
/**
 * Enqueue des CSS / JS / fonts.
 */

defined( 'ABSPATH' ) || exit;

add_action( 'wp_enqueue_scripts', function () {
	$css_path = USAM_THEME_DIR . '/assets/css/main.css';
	$css_ver  = file_exists( $css_path ) ? filemtime( $css_path ) : USAM_THEME_VERSION;

	wp_enqueue_style(
		'usam-main',
		USAM_THEME_URI . '/assets/css/main.css',
		[],
		$css_ver
	);

	$js_path = USAM_THEME_DIR . '/assets/js/main.js';
	if ( file_exists( $js_path ) ) {
		wp_enqueue_script(
			'usam-main',
			USAM_THEME_URI . '/assets/js/main.js',
			[],
			filemtime( $js_path ),
			true
		);
	}
} );

// Fonts self-hosted (à ajouter dans assets/fonts/) — préchargement pour perf.
add_action( 'wp_head', function () {
	$fonts = [
		'Anton-Regular.woff2',
		'Sora-700.woff2',
		'Sora-800.woff2',
		'Inter-400.woff2',
		'Inter-600.woff2',
	];
	foreach ( $fonts as $font ) {
		$path = USAM_THEME_DIR . '/assets/fonts/' . $font;
		if ( file_exists( $path ) ) {
			printf(
				'<link rel="preload" href="%s" as="font" type="font/woff2" crossorigin>%s',
				esc_url( USAM_THEME_URI . '/assets/fonts/' . $font ),
				"\n"
			);
		}
	}
}, 1 );
